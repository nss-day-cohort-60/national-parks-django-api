from django.http import HttpResponseServerError
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Photo, Park, Blog, Event, ParkFavorite, PhotoFavorite, BlogFavorite, EventFavorite
from django.contrib.auth.models import User
from .event_view import EventSerializer
from .photo_view import PhotoSerializer
from .blog_views import BlogSerializer
from .park_view import ParkSerializer

class FavoriteView(ViewSet):
    """Parks API favorites view"""

    def list(self, request):
        """Handle GET requests to get favorites

        Returns:
            Response -- JSON serialized list of favorites
        """

        # need some check for user and some empty return if none?
        try:
            user = request.auth.user
            if "park_id" in request.query_params:
                favorite = ParkFavorite.objects.get(park_id=request.query_params['park_id'],user=user) 
                serialized = ParkFavoriteSerializer(favorite)
            elif "blog_id" in request.query_params:
                favorite = BlogFavorite.objects.get(post_id=request.query_params['blog_id'], user=user )
                serialized = BlogFavoriteSerializer(favorite)
            elif "event_id" in request.query_params:
                favorite = EventFavorite.objects.get(event_id=request.query_params['event_id'], user=user)
                serialized = EventFavoriteSerializer(favorite)
            elif "photo_id" in request.query_params:
                favorite = PhotoFavorite.objects.get(photo_id=request.query_params['photo_id'], user=user)
                serialized = PhotoFavoriteSerializer(favorite)
            elif "parks" in request.query_params:
                favorites = ParkFavorite.objects.filter(user=user).order_by('-id')
                serialized = ParkFavoriteSerializer(favorites, many=True)
            elif "blogs" in request.query_params:
                favorites = BlogFavorite.objects.filter(user=user).order_by('-id')
                serialized = BlogFavoriteSerializer(favorites, many=True)
            elif "events" in request.query_params:
                favorites = EventFavorite.objects.filter(user=user).order_by('-id')
                serialized = EventFavoriteSerializer(favorites, many=True)
            elif "photos" in request.query_params:
                favorites = PhotoFavorite.objects.filter(user=user).order_by('-id')
                serialized = PhotoFavoriteSerializer(favorites, many=True)
        except ObjectDoesNotExist:
            return Response({'valid': False}, status=status.HTTP_404_NOT_FOUND)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handles POST requests for favorites
        Returns:
            Response: JSON serialized representation of newly created favorite"""

        # new_favorite = Favorite()
        # new_favorite.user = request.auth.user
        # new_favorite.save()

        # serialized = FavoriteSerializer(new_favorite, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        """Handle PUT requests for service tickets

        Returns:
            Response: None with 204 status code
        """
        # delete_favorite = Favorite.objects.get(pk=pk)
        # delete_favorite.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PhotoFavoriteSerializer(serializers.ModelSerializer):
    """JSON serializer for favorite photos"""
    photo = PhotoSerializer()

    class Meta:
        model = PhotoFavorite
        fields = ( 'id', 'photo')

class EventFavoriteSerializer(serializers.ModelSerializer):
    """JSON serializer for favorite events"""
    event = EventSerializer()

    class Meta:
        model = EventFavorite
        fields = ('id', 'event')

class ParkFavoriteSerializer(serializers.ModelSerializer):
    """JSON serializer for favorite parks"""
    park = ParkSerializer()

    class Meta:
        model = ParkFavorite
        fields = ( 'id', 'park')

class BlogFavoriteSerializer(serializers.ModelSerializer):
    """JSON serializer for favorite blogs"""
    post = BlogSerializer()

    class Meta:
        model = BlogFavorite
        fields = ('id', 'post')