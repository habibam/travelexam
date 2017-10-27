from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User
import re
import bcrypt

class TripManager(models.Manager):
    def validate(self, post_data):
        results = {"errors": [], "status": False}
        if len(post_data['destination']) < 1:
            results["errors"].append("please enter a destination")
            results["status"] = True

        if len(post_data['description']) < 1:
            results["errors"].append("please enter a description")
            results["status"] = True

        if len(post_data['description']) < 1:
            results["errors"].append("please enter a description")
            results["status"] = True

        return results


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_date_from = models.CharField(max_length=255)
    travel_date_to = models.CharField(max_length=255)
    plan_trip_id = models.ForeignKey(User, related_name="plantrip")
    make_trip_id = models.ManyToManyField(User, related_name="maketrip")
    # owners = models.ManyToManyField(User, related_name='trips')
    travelManager = TripManager()
    objects = models.Manager()

# Create your models here.

