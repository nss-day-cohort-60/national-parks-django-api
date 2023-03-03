from django.db import models

class Wildlife(models.Model):
    name = models.CharField(max_length=255)
    information = models.CharField(max_length=255)
    wildlife_group = models.ForeignKey('WildlifeGroup', on_delete=models.CASCADE, related_name='group_wildlife')
    image = models.CharField(max_length=5000)
    