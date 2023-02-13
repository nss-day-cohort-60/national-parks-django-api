from django.db import models
from django.contrib.auth.models import User


class ParkFavorite(models.Model):
    park = models.ForeignKey("Park", on_delete=models.CASCADE, related_name="favorite_park")
    user = models.OneToOneField(User, on_delete=models.CASCADE)