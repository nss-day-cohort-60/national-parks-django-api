from django.db import models

class Amenity(models.Model):
    type = models.CharField(max_length=255)