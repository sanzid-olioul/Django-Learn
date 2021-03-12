from django.contrib import admin
from .models import BlogsModel
# Register your models here.


@admin.register(BlogsModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","author","date_created","content","comment")