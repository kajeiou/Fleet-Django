from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=20, unique=True)
    mileage = models.IntegerField(default=0)
    last_service_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"

class MaintenanceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenance_records')
    service_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Service on {self.service_date} for {self.vehicle.license_plate}"
