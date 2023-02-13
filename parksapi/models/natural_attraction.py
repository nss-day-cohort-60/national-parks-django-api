from django.db import models

class NaturalAttraction(models.Model):
    name = models.CharField(max_length=50)