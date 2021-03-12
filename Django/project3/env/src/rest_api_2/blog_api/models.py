from django.db import models

from datetime import datetime
# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return self.title