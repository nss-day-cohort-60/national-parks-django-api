from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import ParkNaturalAttraction, NaturalAttraction, Park
from parksapi.views import ParkSerializer

class NaturalAttractionView(ViewSet):
    """Natural Attraction view"""

    def list(self, request):
        """Handle GET requests to get a park by id

        Returns:
            Response -- JSON serialized attraction
        """
        # Get all ParkNaturalAttraction objects
        attractions = ParkNaturalAttraction.objects.all()

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
            attractions = attractions.filter(park=park)

        # Serialize the queryset using the NaturalAttractionSerializer
        serializer = NaturalAttractionSerializer(attractions, many=True)
        # Return the serialized data as a JSON response
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for single park 

        Returns:
            Response -- JSON serialized park 
        """
        attraction = ParkNaturalAttraction.objects.get(pk=pk)
        serializer = NaturalAttractionSerializer(attraction)
        return Response(serializer.data)

        
class AttractionSerializer(serializers.ModelSerializer):
    """JSON serializer for general attractions"""
    class Meta:
        model = NaturalAttraction
        fields = ('id', 'name')

class NaturalAttractionSerializer(serializers.ModelSerializer):
    """JSON serializer for Park natural attractions"""
    park = ParkSerializer(many=False)
    attraction = AttractionSerializer(many=False)

    class Meta:
        model = ParkNaturalAttraction
        fields = ('id', 'name', 'description', 'park', 'attraction')