from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    dept = models.CharField(max_length=50)
    roll = models.IntegerField()
    cgpa = models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return str(self.roll)
    #name age dept roll cgpa