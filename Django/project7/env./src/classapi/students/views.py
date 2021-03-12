from re import S
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework.views import APIView

class StudentsView(APIView):
    def get(self,request):
        dta = StudentModel.objects.all()
        serialier = StudentSerializers(dta,many = True)
        
        return Response(serialier.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serialier = StudentSerializers(data=request.data)
        if serialier.is_valid():
            serialier.save()
            return Response(serialier.data,status=status.HTTP_201_CREATED)