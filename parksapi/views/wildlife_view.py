from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Wildlife, ParkWildlife, WildlifeGroup


class WildlifeView(ViewSet):
    """National Park API wildlife view"""

    def list(self, request):
        """Handle GET requests to get all wildlife

        Returns:
            Response -- JSON serialized list of wildlife
        """
        if "park_id" in request.query_params:
            try:
                park_wildlife = ParkWildlife.objects.all()
                filtered = park_wildlife.filter(
                    park_id=request.query_params.get('park_id'))
                assert len(filtered) > 0
            except AssertionError:
                return Response({'message': 'Invalid park id'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ParkWildlifeSerializer(filtered, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        all_wildlife = Wildlife.objects.all()
        serializer = WildlifeSerializer(all_wildlife, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle GET requests for single wildlife

        Returns:
            Response -- JSON serialized wildlife
        """
        try:
            wildlife = Wildlife.objects.get(pk=pk)
        except Wildlife.DoesNotExist:
            return Response({'message': 'You sent an invalid wildlife ID'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WildlifeSerializer(wildlife)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST operations for wildlife"""
        try:
            wildlife_group = WildlifeGroup.objects.get(
                pk=request.data["wildlife_group"])

            wildlife = Wildlife()
            wildlife.name = request.data["name"]
            wildlife.information = request.data["information"]
            wildlife.wildlife_group = wildlife_group
            wildlife.image = request.data['image']
        except KeyError as err:
            return Response({'message':"key "+str(err)+" is missing"}, status=status.HTTP_400_BAD_REQUEST)
        
        wildlife.save()
        serializer = WildlifeSerializer(wildlife)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for wildlife
        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            wildlife_group = WildlifeGroup.objects.get(pk=request.data["wildlife_group"])

            wildlife = Wildlife.objects.get(pk=pk)
            wildlife.name = request.data['name']
            wildlife.information = request.data['information']
            wildlife.wildlife_group = wildlife_group
            wildlife.image= request.data['image']
        except KeyError as err:
            return Response({'message': "key "+str(err)+" is missing"}, status=status.HTTP_400_BAD_REQUEST)
        
        wildlife.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests for events

        Returns:
            Response: None with 204 status code
        """
        wildlife = Wildlife.objects.get(pk=pk)
        wildlife.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class WildlifeSerializer(serializers.ModelSerializer):
    """JSON serializer for wildlife
    """
    class Meta:
        model = Wildlife
        fields = ('id', 'name', 'information', 'wildlife_group', 'image')


class ParkWildlifeSerializer(serializers.ModelSerializer):
    """JSON serializer for parkwildlife
    """
    class Meta:
        model = ParkWildlife
        fields = ('wildlife',)
        depth=1
