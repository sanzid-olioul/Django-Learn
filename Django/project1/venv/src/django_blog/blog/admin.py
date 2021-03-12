import django
from django.contrib import admin

from .models import ArticleModel
# Register your models here.
@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author","time_created")