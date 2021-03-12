from django.contrib import admin

from .models import UserInfoModel
# Register your models here.
@admin.register(UserInfoModel)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("first_name","email","gender","date_of_birth")