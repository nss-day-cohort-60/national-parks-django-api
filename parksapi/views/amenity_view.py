from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Amenity, ParkAmenity


class AmenityView(ViewSet):
    """National Park API amenity view"""

    def list(self, request):
        """Handle GET requests to get all amenities

        Returns:
            Response -- JSON serialized list of amenities
        """
        if "park_id" in request.query_params:
            try:
                park_amenity = ParkAmenity.objects.all()
                filtered = park_amenity.filter(
                    park_id=request.query_params.get('park_id'))
                assert len(filtered) > 0
            except AssertionError:
                return Response({'message': 'Invalid park id'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ParkAmenitySerializer(filtered, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        amenities = Amenity.objects.all()
        serializer = AmenitySerializer(amenities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle GET requests for single amenity

        Returns:
            Response -- JSON serialized amenity
        """
        try:
            amenity = Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            return Response({'message': 'You sent an invalid amenity ID'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AmenitySerializer(serializers.ModelSerializer):
    """JSON serializer for amenity
    """
    class Meta:
        model = Amenity
        fields = ('id', 'type')


class ParkAmenitySerializer(serializers.ModelSerializer):
    """JSON serializer for parkamenity
    """
    class Meta:
        model = ParkAmenity
        fields = ('name', 'amenity','park')
      
