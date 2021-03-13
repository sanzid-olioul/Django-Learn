from re import S
from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializer

from rest_framework import generics
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer