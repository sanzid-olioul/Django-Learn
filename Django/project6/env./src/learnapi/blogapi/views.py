from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BlogsModel
from .serializers import BlogsSerializer
# Create your views here.
@api_view(['GET','POST'])
def home_view(request,*args,**kwargs):
    # datas = {
    #     "name":"Sanzid Olioul Tanzid",
    #     "uni": "Pabna University of Science and technology",
    #     "session":"2018-19",
    #     "dept":"CSE"
    # }
    if request.method == 'GET':
        blg = BlogsModel.objects.all()

        # dta = {'blog': list(blg.values('title','author','content'))}
        serializer = BlogsSerializer(blg,many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BlogsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)