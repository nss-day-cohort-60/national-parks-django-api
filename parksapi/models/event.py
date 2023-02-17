from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event_type = models.ForeignKey("EventType", default=6, on_delete=models.CASCADE, related_name="event_type")
    park = models.ForeignKey("Park", on_delete=models.CASCADE, related_name='park_events')
