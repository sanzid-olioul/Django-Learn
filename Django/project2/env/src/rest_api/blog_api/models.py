from django.db import models
from django.db.models.base import Model

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.CharField(max_length=8)
    weight = models.FloatField()
    institute = models.CharField(max_length=120)

    def __str__(self):
        return self.name