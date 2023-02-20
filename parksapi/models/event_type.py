from django.db import models

class EventType(models.Model):
    type = models.CharField(max_length=50)

