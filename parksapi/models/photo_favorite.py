from django.db import models
from django.contrib.auth.models import User


class PhotoFavorite(models.Model):
    photo = models.ForeignKey("Photo", on_delete=models.CASCADE, related_name="favorite_photo")
    user = models.OneToOneField(User, on_delete=models.CASCADE)