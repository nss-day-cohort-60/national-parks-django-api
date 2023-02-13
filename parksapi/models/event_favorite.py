from django.db import models

class EventFavorite(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="favorite_event")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_event_favorite")