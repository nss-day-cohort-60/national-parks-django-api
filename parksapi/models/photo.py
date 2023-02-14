from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    url = models.CharField(max_length=800)
    park = models.ForeignKey('Park', on_delete=models.CASCADE, related_name='park_photos')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')