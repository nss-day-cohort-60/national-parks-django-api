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

        if "park_id" in request.query_params:
            blogs = Blog.objects.filter(park=request.query_params['park_id'])
        elif "user_id" in request.query_params:
            blogs = Blog.objects.filter(user=request.query_params['user_id'])
        else:
            blogs = Blog.objects.all()

        serialized = BlogSerializer(blogs, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handles POST requests for blogs
        Returns:
            Response: JSON serialized representation of newly created blog"""
        
        new_blog = Blog()
        new_blog.title = request.data['title']
        new_blog.post_body = request.data['post_body']
        new_blog.date_created= request.data['date_created']
        new_blog.park = Park.objects.get(pk=request.data['park'])
        new_blog.photo = Photo.objects.get(pk=request.data['photo'])
        new_blog.user = request.auth.user
        new_blog.save()

        serialized = BlogSerializer(new_blog, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for blogs

        Returns:
            nothing
        """

        edit_blog = Blog.objects.get(pk=pk)
        edit_blog.title = request.data['title']
        edit_blog.post_body = request.data['post_body']
        edit_blog.park = Park.objects.get(pk=request.data['park'])
        edit_blog.photo = Photo.objects.get(pk=request.data['photo'])
        edit_blog.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle PUT requests for service tickets

        Returns:
            Response: None with 204 status code
        """
        delete_blog = Blog.objects.get(pk=pk)
        delete_blog.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BlogPhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for blog photos"""
    class Meta:
        model = Photo
        fields = ('id', 'url')

class BlogUserSerializer(serializers.ModelSerializer):
    """JSON serializer for blog users"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

class BlogParkSerializer(serializers.ModelSerializer):
    """JSON serializer for blog parks"""
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