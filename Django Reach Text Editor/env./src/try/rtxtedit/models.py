from django.db import models
from django.db.models.fields import CharField
from ckeditor.fields import RichTextField
# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=True)
    article = RichTextField(blank = True, null = True)

    def __str__(self):
        return self.title