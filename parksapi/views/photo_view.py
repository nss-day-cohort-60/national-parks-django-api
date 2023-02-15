"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers, status
from parksapi.models import Photo, Park

class PhotoView(ViewSet):
    """National Parks API photo view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single photo

        Returns:
            Response -- JSON serialized photo
        """

        try: 
            photo = Photo.objects.get(pk=pk)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        except Photo.DoesNotExist as ex: 
            return Response({'message:': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all photos

        Returns:
            Response -- JSON serialized list of photos
        """

        photos = Photo.objects.all()
        
        if "park_id" in request.query_params:
            photos = photos.filter(park=request.query_params['park_id'])

            if "user_id" in request.query_params:    
                photos = photos.filter(user=request.query_params['user_id'])

        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized photo instance
        """
        # {
        #     "url": "https://res.cloudinary.com/dcuwovsbv/image/upload/v1676470586/National-Parks/Park-Photos/Joshua-Tree-Weekend-Barker-Dam_wuezzl.jpg",
        #     "park": 1
        # }       

        # park = Park.objects.get(pk=request.data["park"])
        # user=request.auth.user
        # serializer = CreatePhotoSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save(park=park, user=user)

        photo = Photo.objects.create(
            url=request.data["url"],
            park=Park.objects.get(pk=request.data["park"]),
            user=request.auth.user
        )
        serializer = PhotoSerializer(photo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ParkPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ['id', 'name', ] 

class CreatePhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for creating a photo
    """

    class Meta:
        model = Photo
        fields = ('url', 'park')

class PhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for photos
    """
    park = ParkPhotoSerializer(many=False)

    class Meta:
        model = Photo
        fields = ('id', 'url', 'park', 'user', )
