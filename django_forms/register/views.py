from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .form import RegisterForm,LoginForm
# Create your views here.

class Login(View):
    def get(self,request,*args,**kwargs):
        frm = LoginForm()
        return render(request,'login.html',{'form':frm})
    def post(self,request,*args,**kwargs):
        email =request.POST.get('email','')
        password = request.POST.get('password','')
        print(email,password)
        return HttpResponse('Got your data')


class Register(View):
    def get(self,request,*args,**kwargs):
        frm = RegisterForm()
        return render(request,'register.html',{'form':frm})
    def post(self,request,*args,**kwargs):
        f_name = request.POST.get('f_name','')
        l_name = request.POST.get('l_name','')
        email =request.POST.get('email','')
        password = request.POST.get('password','')
        print(f_name,l_name,email,password)
        return HttpResponse('Got your data')
