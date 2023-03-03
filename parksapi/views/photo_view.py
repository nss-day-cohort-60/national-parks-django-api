"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers, status
from parksapi.models import Photo, Park
# imports below here for photo migration from cloudinary
from django.core.files.base import ContentFile
from django.core.files import File
from urllib.request import urlopen
from io import BytesIO
from PIL import Image
import os

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
        # temporary file migration from cloudinary on photo fetch
        # photo_list = Photo.objects.all()

        # for photo in photo_list:
        #     if not photo.image:
        #         try:
        #             response = urlopen(photo.url)
        #             image_data = response.read()
        #             image = Image.open(BytesIO(image_data))
        #             photo.image.save(os.path.basename(photo.url), content=ContentFile(image_data), save=True)
        #         except:
        #             pass
        # temporarily override normal fetch for file migration from cloudinary on photo fetch
        
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
        serializer = CreatePhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        park = Park.objects.get(pk=request.data["park"])
        user=request.auth.user
        serializer.save(park=park, user=user)
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
        fields = ('id', 'url', 'image', 'park', 'user', )
