from django.db import models

# Create your models here.
class UserInfoModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=50)
    date_of_birth= models.DateField()

    def __str__(self) :
        return self.email