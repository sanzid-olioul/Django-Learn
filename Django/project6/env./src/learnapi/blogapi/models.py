from django.db import models

# Create your models here.
class BlogsModel(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    date_created = models.DateField()
    content = models.TextField()
    comment = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title