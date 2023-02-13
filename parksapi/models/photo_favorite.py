from django.db import models

class PhotoFavorite(models.Model):
    photo = models.ForeignKey("Photo", on_delete=models.CASCADE, related_name="favorite_photo")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_favorite_photo")