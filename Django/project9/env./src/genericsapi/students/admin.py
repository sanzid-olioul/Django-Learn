from re import S
from django.contrib import admin

from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("uni", "dept","age","birth","married")



#"uni", "dept","age","birth","married"


