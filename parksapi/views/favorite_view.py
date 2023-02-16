from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Favorite, Photo, Park, Blog, Event, ParkFavorite, PhotoFavorite, BlogFavorite, EventFavorite
from django.contrib.auth.models import User
from datetime import datetime

class FavoriteView(ViewSet):
    """Parks API favorites view"""
    def retrieve(self, request, pk):
        """Handle GET requests for single blog

        Returns:
            Response -- JSON serialized blog
        """
                # need some check for user and some empty return if none?
        user = request.auth.user
        if "park_id" in request.query_params:
            favorite = ParkFavorite.objects.get(pk=request.query_params['park_id'],user=user) 
            serialized = ParkFavoriteSerializer(favorite)
        elif "blog_id" in request.query_params:
            favorite = BlogFavorite.objects.get(pk=request.query_params['blog_id'], user=user )
            serialized = BlogFavoriteSerializer(favorite)
        elif "event_id" in request.query_params:
            favorite = EventFavorite.objects.get(pk=request.query_params['event_id'], user=user)
            serialized = EventFavoriteSerializer(favorite)
        elif "photo_id" in request.query.params:
            favorite = PhotoFavorite.objects.get(pk=request.query_params['photo_id'], user=user)
            serialized = PhotoFavoriteSerializer(favorite)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get many favorites

        Returns:
            Response -- JSON serialized list of tickets
        """

        # need some check for user and some empty return if none?
        user = request.auth.user
        if "parks" in request.query_params:
            favorites = ParkFavorite.objects.filter(user=user).order_by('-date_created')
            serialized = ParkFavoriteSerializer(favorites, many=True)
        elif "blogs" in request.query_params:
            favorites = BlogFavorite.objects.filter(user=user).order_by('-date_created')
            serialized = BlogFavoriteSerializer(favorites, many=True)
        elif "events" in request.query_params:
            favorites = EventFavorite.objects.filter(user=user).order_by('-date_created')
            serialized = EventFavoriteSerializer(favorites, many=True)
        elif "photos" in request.query.params:
            favorites = PhotoFavorite.objects.filter(user=user).order_by('-date_created')
            serialized = PhotoFavoriteSerializer(favorites, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handles POST requests for favorites
        Returns:
            Response: JSON serialized representation of newly created favorite"""

        new_favorite = Favorite()
        new_favorite.user = request.auth.user
        new_favorite.save()

        serialized = FavoriteSerializer(new_favorite, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        """Handle PUT requests for service tickets

        Returns:
            Response: None with 204 status code
        """
        delete_favorite = Favorite.objects.get(pk=pk)
        delete_favorite.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PhotoFavoriteSerializer(serializers.ModelSerializer):
    """JSON serializer for favorite photos"""
    class Meta:
        model = Photo
        fields = ('id', 'url')

class EventFavoriteSerializer(serializers.ModelSerializer):
    """JSON serializer for favorite events"""
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'start_date', 'park_id')

class ParkFavoriteSerializer(serializers.ModelSerializer):
    """JSON serializer for favorite parks"""
    class Meta:
        model = Park
        fields = ('id', 'name')

class FavoriteSerializer(serializers.ModelSerializer):
    """JSON serializer for songs"""

    class Meta:
        model = Favorite
        fields = ('id', 'title', 'post_body', 'date_created', 'user', 'park', 'photo')
        depth = 1