from django.db import models
from django.contrib.auth.models import User


class CampingReservation(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    campground = models.ForeignKey('Campground', on_delete=models.CASCADE, related_name='reserved_campgrounds')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reservations')
