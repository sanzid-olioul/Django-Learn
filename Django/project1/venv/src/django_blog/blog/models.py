from django.db import models
from django.utils import timezone

from django.db.models.fields import TextField
# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    time_created = models.DateTimeField(default=timezone.now())
    post = TextField()
    
    def __str__(self):
        return self.title