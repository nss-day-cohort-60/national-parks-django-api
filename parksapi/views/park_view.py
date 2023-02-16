from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Park

class ParkView(ViewSet):
    """Parks Park view"""

    def create(self, request):
        """Handle POST operations for parks"""

        park = Park()
        park.name = request.data["name"]
        park.history = request.data["history"]
        park.city = request.data["city"]
        park.state = request.data["state"]
        park.longitude = request.data["longitude"]
        park.latitude = request.data['latitude']

        try:
            park.save()
            serializer = ParkSerializer(park, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, park_id=None):
        """Handle GET requests to get a park by id or all parks

        Returns:
            Response -- JSON serialized park 
        """
        if park_id:
            try:
                park = Park.objects.get(park_id=park_id)
            except Park.DoesNotExist:
                return Response({"error": "Park not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = ParkSerializer(park)
            return Response(serializer.data)
        else:
            parks = Park.objects.all()
            serializer = ParkSerializer(parks, many=True)
            return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for single park 

        Returns:
            Response -- JSON serialized park 
        """
        park = Park.objects.get(pk=pk)
        serializer = ParkSerializer(park)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        park = Park.objects.get(pk=pk)
        park.name = request.data['name']
        park.history = request.data['history']
        park.city = request.data['city']
        park.state = request.data['state']
        park.longitude = request.data['longitude']
        park.latitude = request.data['latitude']
        park.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        park = Park.objects.get(pk=pk)
        park.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class ParkSerializer(serializers.ModelSerializer):
    """JSON serializer for parks"""
    class Meta:
        model = Park
        fields = ('id', 'name', 'history',
                  'city', 'state', 'longitude',
                  'latitude')