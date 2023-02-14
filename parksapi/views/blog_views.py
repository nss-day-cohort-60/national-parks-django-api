from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Blog, Photo, Park
from django.contrib.auth.models import User


class BlogView(ViewSet):
    """Parks API blogs view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single blog

        Returns:
            Response -- JSON serialized blog
        """
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all blogs

        Returns:
            Response -- JSON serialized list of tickets
        """

        blogs=[]

        if "park" in request.query_params:
            blogs = Blog.objects.all()
            if request.query_params['park']=="joshua-tree":
                blogs = blogs.filter(park=1)
            if request.query_params['park'] == "everglades":
                blogs = blogs.filter(park=2)
            if request.query_params['park'] == "great-smoky-mountains":
                blogs = blogs.filter(park=3)
            if request.query_params['park'] == "haleakala":
                blogs = blogs.filter(park=4)
            if request.query_params['park'] == "yosemite":
                blogs = blogs.filter(park=5)
            if request.query_params['park'] == "glacier":
                blogs = blogs.filter(park=6)
            if request.query_params['park'] == "kenai-fjords":
                blogs = blogs.filter(park=7)
            if request.query_params['park'] == "shenandoah":
                blogs = blogs.filter(park=8)
            if request.query_params['park'] == "saguaro":
                blogs = blogs.filter(park=9)
        elif "user" in request.query_params:
            blogs = Blog.objects.filter(user=request.query_params['user'])
        else:
            blogs = Blog.objects.all()

        serialized = BlogSerializer(blogs, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

class BlogPhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for blog photos"""
    class Meta:
        model = Photo
        fields = ('id', 'url')

class BlogUserSerializer(serializers.ModelSerializer):
    """JSON serializer for blog photos"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

class BlogParkSerializer(serializers.ModelSerializer):
    """JSON serializer for blog photos"""
    class Meta:
        model = Park
        fields = ('id', 'name')


class BlogSerializer(serializers.ModelSerializer):
    """JSON serializer for songs"""

    user = BlogUserSerializer(many=False)
    photo = BlogPhotoSerializer(many=False)
    park = BlogParkSerializer(many=False)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'post_body', 'date_created', 'user', 'park', 'photo')
        depth = 1