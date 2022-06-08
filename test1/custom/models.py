from django.utils import timezone
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to = "images")
    content = models.TextField()
    is_deleted = models.BooleanField(default = False)
    published_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title
    def days_since_created(self):
        diff = timezone.now() - self.published_date

        return diff.days 