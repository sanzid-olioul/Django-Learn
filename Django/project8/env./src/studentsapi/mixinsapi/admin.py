from django.contrib import admin
from .models import StudentModel
# Register your models here.
@admin.register(StudentModel)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'dept', 'roll', 'cgpa')