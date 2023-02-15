from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Blog, Photo, Park
from django.contrib.auth.models import User
from datetime import datetime

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

        if "key_word" in request.query_params:
            if "park_id" in request.query_params:
                blogs = Blog.objects.filter(
                    Q(park=request.query_params['park_id']),
                    Q(title__contains=request.query_params['key_word']) 
                    | Q(post_body__contains=request.query_params['key_word'])).order_by('-date_created')
            else:
                blogs = Blog.objects.filter(Q(title__contains=request.query_params['key_word']) | Q(post_body__contains=request.query_params['key_word'])).order_by('-date_created')

        elif "park_id" in request.query_params:
            blogs = Blog.objects.filter(park=request.query_params['park_id']).order_by('-date_created')
        elif "user_id" in request.query_params:
            blogs = Blog.objects.filter(user=request.query_params['user_id']).order_by('-date_created')
        else:
            blogs = Blog.objects.all().order_by('-date_created')

        serialized = BlogSerializer(blogs, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handles POST requests for blogs
        Returns:
            Response: JSON serialized representation of newly created blog"""

        new_blog = Blog()
        new_blog.title = request.data['title']
        new_blog.post_body = request.data['post_body']
        new_blog.date_created= datetime.now().strftime('%Y-%m-%d %H:%M')
        new_blog.park = Park.objects.get(pk=request.data['park_id'])
        try:
            new_blog.photo = Photo.objects.get(url=request.data['photo_url'])
        except Photo.DoesNotExist:
            pass
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
        edit_blog.park = Park.objects.get(pk=request.data['park']['id'])
        try:
            edit_blog.photo = Photo.objects.get(pk=request.data['photo'])
        except Photo.DoesNotExist:
            pass
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