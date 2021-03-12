from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from .serializers import BlogSerializer
from .models import BlogModel

from django.views import View
class Home(View):
    def get(self,request):
        data = BlogModel.objects.all()
        serial = BlogSerializer(data,many = True)
        jsonData = JsonResponse(serial.data,safe=False)
        print(jsonData)
        return HttpResponse(jsonData,content_type = "application/json")
        #return HttpResponse("working...")
    
    def post(self,request):
        return HttpResponse('Welcome bro ... come come...')