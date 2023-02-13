from django.db import models
from django.contrib.auth.models import User
from models import Event


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attending_events')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_events')
