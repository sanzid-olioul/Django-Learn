from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    uni = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    age = models.IntegerField()
    birth = models.DateField()  
    married = models.CharField(max_length=5 , choices=[("yes",("Yes")),("no",("No"))])

    def __str__(self):
        return self.name