from django.db import models

class ParkNaturalAttraction(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    park = models.ForeignKey("Park", on_delete=models.CASCADE, related_name="attractions_by_park")
    attraction = models.ForeignKey("NaturalAttraction", on_delete=models.CASCADE, related_name="attraction_types")