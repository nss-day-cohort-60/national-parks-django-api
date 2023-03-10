from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Event, Park, EventType, EventRegistration
from django.contrib.auth.models import User


class EventView(ViewSet):
    """Parks API blogs view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serialized event
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """

        events=[]

        if "park_id" in request.query_params:
            events = Event.objects.filter(park=request.query_params['park_id'])
        else:
            events = Event.objects.all()

        serialized = EventSerializer(events, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handles POST requests for blogs
        Returns:
            Response: JSON serialized representation of newly created blog"""
        if "register" in request.data:
            new_registration = EventRegistration()
            new_registration.user = request.auth.user
            new_registration.event = Event.objects.get(pk=request.data['id'])
            new_registration.save()
            serialized = EventRegistrationSerializer(new_registration)
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            new_event = Event()
            new_event.name = request.data['name']
            new_event.description = request.data['description']
            new_event.start_date= request.data['start_date']
            new_event.end_date = request.data['end_date']
            new_event.event_type = EventType.objects.get(pk=request.data['event_type'])
            new_event.park = Park.objects.get(pk=request.data['park'])
            new_event.save()

            serialized = EventSerializer(new_event, many=False)

            return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for blogs

        Returns:
            nothing
        """

        edit_event = Event.objects.get(pk=pk)
        edit_event.name = request.data['name']
        edit_event.description = request.data['description']
        edit_event.start_date= request.data['start_date']
        edit_event.event_type = EventType.objects.get(pk=request.data['event_type'])
        edit_event.park = Park.objects.get(pk=request.data['park'])
        edit_event.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle PUT requests for service tickets

        Returns:
            Response: None with 204 status code
        """
        delete_event = Event.objects.get(pk=pk)
        delete_event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ('id', 'user', 'event')

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ('id', 'type')
class EventParkSerializer(serializers.ModelSerializer):
    """JSON serializer for blog parks"""
    class Meta:
        model = Park
        fields = ('id', 'name')

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for songs"""
    park = EventParkSerializer(many=False)
    event_type = EventTypeSerializer
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'event_type', 'park')
        depth = 1