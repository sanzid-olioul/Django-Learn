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
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'],form.cleaned_data['pasword'])
            return HttpResponse('Got your data')
        return render(request,'login.html',{'form':form})


class Register(View):
    def get(self,request,*args,**kwargs):
        frm = RegisterForm()
        return render(request,'register.html',{'form':frm})
    def post(self,request,*args,**kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            print(form.cleaned_data['f_name'],form.cleaned_data['l_name'],form.cleaned_data['email'],form.cleaned_data['pasword'])
            return HttpResponse('Got your data')
        return render(request,'register.html',{'form':form})
