from django.shortcuts import render
from .models import BlogModel
from .serializers import BlogSerializers
# Create your views here.
from rest_framework import generics

class HomeView(generics.ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers