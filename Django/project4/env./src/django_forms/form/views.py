from django.shortcuts import render
from django.views import View
# Create your views here.
class Form(View):
    def get(self,request):
        return render(request,'index.html',{})

    def post(self,request):
        pass