from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from . serializers import StudentSerializer
from . models import StudentModel
# Create your views here.
def home_view(request):
    stu = StudentModel.objects.all()
    serial = StudentSerializer(stu,many = True)

    #JsonResponse(serial.data) does the same thing bellow two line
    json_deta = JSONRenderer().render(serial.data)
    return HttpResponse(json_deta,content_type = "application/json")