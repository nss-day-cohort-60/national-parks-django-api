from django.db import models
from django.contrib.auth.models import User

class BlogFavorite(models.Model):
    post = models.ForeignKey("Blog", on_delete=models.CASCADE, related_name="favorite_blog")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_favorite_blog")