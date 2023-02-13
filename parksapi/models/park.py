from django.db import models

class Park(models.Model):
    name = models.CharField(max_length=255)
    history = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
