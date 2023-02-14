"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Photo, Park

class PhotoView(ViewSet):
    """National Parks API photo view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single photo

        Returns:
            Response -- JSON serialized photo
        """

        photo = Photo.objects.get(pk=pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

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

        # url, park, and user

        photo = Photo.objects.create(
            url=request.data["url"],
            park=Park.objects.get(pk=request.data["park_id"]),
            user=request.auth.user
        )

        serializer = PhotoSerializer(photo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ParkPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ['id', 'name', ] 

class PhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for photos
    """
    park = ParkPhotoSerializer(many=False)

    class Meta:
        model = Photo
        fields = ('id', 'url', 'park', 'user', )
