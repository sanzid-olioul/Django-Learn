from django.db import models

# Create your models here.
class UserRegister(models.Model):
    f_name = models.CharField(max_length = 50)
    l_name = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length = 50 )

class UserLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 50)
