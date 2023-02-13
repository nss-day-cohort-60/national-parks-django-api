from django.db import models

class ParkFavorite(models.Model):
    park = models.ForeignKey("Park", on_delete=models.CASCADE, related_name="favorite_park")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_park_favorite")