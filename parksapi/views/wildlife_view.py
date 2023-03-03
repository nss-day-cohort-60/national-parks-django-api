from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Wildlife, ParkWildlife, WildlifeGroup
# imports below here for photo migration from cloudinary
from django.core.files.base import ContentFile
from django.core.files import File
from urllib.request import urlopen
from io import BytesIO
from PIL import Image
import os

class WildlifeView(ViewSet):
    """National Park API wildlife view"""

    def list(self, request):
        """Handle GET requests to get all wildlife

        Returns:
            Response -- JSON serialized list of wildlife
        """
        # temporary file migration from cloudinary on wildlife fetch
        wildlife_list = Wildlife.objects.all()

        for wildlife in wildlife_list:
            if not wildlife.image:
                try:
                    response = urlopen(wildlife.url)
                    image_data = response.read()
                    image = Image.open(BytesIO(image_data))
                    wildlife.image.save(os.path.basename(wildlife.url), content=ContentFile(image_data), save=True)
                except:
                    pass
        # temporarily override normal fetch for file migration from cloudinary on wildlife fetch

        # if "park_id" in request.query_params:
        #     try:
        #         park_wildlife = ParkWildlife.objects.all()
        #         filtered = park_wildlife.filter(
        #             park_id=request.query_params.get('park_id'))
        #         filtered = [x.wildlife for x in filtered]
        #         assert len(filtered) > 0
        #     except AssertionError:
        #         return Response({'message': 'Invalid park id'}, status=status.HTTP_404_NOT_FOUND)
        #     serializer = WildlifeSerializer(filtered, many=True)
        #     return Response(serializer.data, status=status.HTTP_200_OK)
    
        # all_wildlife = Wildlife.objects.all()
        # serializer = WildlifeSerializer(all_wildlife, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

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


