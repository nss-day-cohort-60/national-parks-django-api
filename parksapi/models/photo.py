from django.db import models

class Photo(models.Model):
    url = models.CharField(max_length=800)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_photos")