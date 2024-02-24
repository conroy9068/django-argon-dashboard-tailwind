from django.db import models


class Vehicle(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    spec = models.CharField(max_length=255, blank=True)
    reg_no = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    vin = models.CharField(max_length=255)
    engine_no = models.CharField(max_length=255)
    # ... include other fields as per form

class Assessment(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    engineer_name = models.CharField(max_length=255)
    date = models.DateField()
    membership_number = models.CharField(max_length=255)
    # ... include other fields as per form

class RepairItem(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    description = models.TextField()
    action = models.CharField(max_length=255)
    # ... include other fields as per form
