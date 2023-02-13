from django.db import models

class ParkWildlife(models.Model):
    park = models.ForeignKey("Park", on_delete=models.CASCADE, related_name="wildlife_at_park")
    wildlife = models.ForeignKey("Wildlife", on_delete=models.CASCADE, related_name="wildlife")