from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Campground, CampingReservation, Park
from parksapi.views import ParkSerializer
# imports below here for photo migration from cloudinary
from django.core.files.base import ContentFile
from django.core.files import File
from urllib.request import urlopen
from io import BytesIO
from PIL import Image
import os

class CampgroundView(ViewSet):
    """campground views"""

    def list(self, request):
        """Handle GET requests to get a park by id

        Returns:
            Response -- JSON serialized attraction
        """
        # temporary file migration from cloudinary on campground fetch
        # campground_list = Campground.objects.all()

        # for campground in campground_list:
            
        #     try:
        #         response = urlopen(campground.url)
        #         image_data = response.read()
        #         image = Image.open(BytesIO(image_data))
        #         campground.image.save(os.path.basename(campground.url), content=ContentFile(image_data), save=True)
        #     except:
        #         pass
        # temporarily override normal fetch for file migration from cloudinary on campground fetch

        # Get all ParkNaturalAttraction objects
        campgrounds = Campground.objects.all()

        if "park_id" in request.query_params:
            # Get the park_id parameter from the query string
            park_id = request.query_params['park_id']

            try:
                # Attempt to get the Park object with the specified ID
                park = Park.objects.get(id=park_id)

            except Park.DoesNotExist:
                # If the park is not found, return a 404 error response
                return Response({"error": "park not found"}, status=status.HTTP_404_NOT_FOUND)

            # Filter the attractions queryset by the specified park
            campgrounds = campgrounds.filter(park=park)

        # Serialize the queryset using the NaturalAttractionSerializer
        serializer = NaturalAttractionSerializer(campgrounds, many=True)
        # Return the serialized data as a JSON response
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for single park 

        Returns:
            Response -- JSON serialized park 
        """
        attraction = Campground.objects.get(pk=pk)
        serializer = NaturalAttractionSerializer(attraction)
        return Response(serializer.data)

        

class NaturalAttractionSerializer(serializers.ModelSerializer):
    """JSON serializer for Park natural attractions"""
    park = ParkSerializer(many=False)

    class Meta:
        model = Campground
        fields = ('id', 'name', 'park', 'available_sites', 'description', 'image')