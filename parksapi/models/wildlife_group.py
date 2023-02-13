from django.db import models

class WildlifeGroup(models.Model):
    name = models.CharField(max_length=255)