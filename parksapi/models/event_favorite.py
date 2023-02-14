from django.db import models
from django.contrib.auth.models import User


class EventFavorite(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="favorite_event")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favorite_events')