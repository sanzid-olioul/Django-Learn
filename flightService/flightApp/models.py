from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.urls.conf import path

# Create your models here.
class Flight(models.Model):
    floghtNumber = models.CharField(max_length=15)
    operatingAirlines = models.CharField(max_length=25)
    departureCity = models.CharField(max_length=25)
    arrivalCity = models.CharField(max_length=25)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

    def __str__(self):
        return self.floghtNumber

class Passenger(models.Model):
    firstNmae = models.CharField(max_length=25)
    lastNmae = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.firstNmae

class Reservation(models.Model):
    flight = models.OneToOneField(Flight,on_delete=CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)

    def __str__(self):
        return self.flight.floghtNumber
