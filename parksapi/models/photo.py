from django.db import models

class Photo(models.Model):
    url = models.CharField(max_length=800)
    user = models.OneToOneField('User', on_delete=models.CASCADE)