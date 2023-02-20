from django.db import models


class Campground(models.Model):
    name = models.CharField(max_length=150)
    park = models.ForeignKey("Park", on_delete=models.CASCADE, related_name="park_campgrounds")
    available_sites = models.IntegerField()
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=5000)
