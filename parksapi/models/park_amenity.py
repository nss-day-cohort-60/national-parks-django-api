from django.db import models

class ParkAmenity(models.Model):
    name = models.CharField(max_length=255, null=True)
    amenity = models.ForeignKey('Amenity', on_delete=models.CASCADE, related_name='type_amenities')
    park = models.ForeignKey('Park', on_delete=models.CASCADE, related_name='park_amenities')
