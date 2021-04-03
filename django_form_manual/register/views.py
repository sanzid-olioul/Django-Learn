from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .form import RegisterForm
# Create your views here.

def register_view(request,*args,**kwargs):
    if request.method == 'POST':
        print(request.POST)
        return HttpResponse("Got the result")
    if request.method == 'GET':
        frm = RegisterForm()
    
    return render(request,'test.html',{'form':frm})

class Login(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')
    def post(self,request,*args,**kwargs):
        email =request.POST.get('email','')
        password = request.POST.get('password','')
        print(email,password)
        return HttpResponse('Got your data')


class Register(View):
    def get(self,request,*args,**kwargs):
        return render(request,'register.html')
    def post(self,request,*args,**kwargs):
        email =request.POST.get('email','')
        password = request.POST.get('password','')
        first_name =request.POST.get('first_name','')
        last_name = request.POST.get('last_name','')

        print(first_name,last_name,email,password)
        return HttpResponse('Got your data')
