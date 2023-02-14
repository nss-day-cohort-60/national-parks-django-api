from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Wildlife, Park


class WildlifeView(ViewSet):
    """National Park API wildlife view"""

    def list(self, request):
        """Handle GET requests to get all wildlife

        Returns:
            Response -- JSON serialized list of wildlife
        """
        try:
            all_wildlife = Wildlife.objects.all()
            if "park_id" in request.query_params:
                all_wildlife = all_wildlife.filter(park_id=request.query_params['park_id'])
                return Response({'message': 'You sent an invalid park ID'}, status=status.HTTP_404_NOT_FOUND)
        except Wildlife.DoesNotExist:
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

    
class WildlifeSerializer(serializers.ModelSerializer):
    """JSON serializer for wildlife
    """
    class Meta:
        model = Wildlife
        fields = ('id', 'name', 'information', 'wildlife_group', 'image')
