from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    park = models.ForeignKey("Park", on_delete=models.CASCADE, related_name='park_events')
