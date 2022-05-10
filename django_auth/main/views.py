from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth import authenticate, login,logout
from django.views import View

from .form import RegisterForm,LoginForm
# Create your views here.
# @login_required(login_url='user/login')
class Home(View):
    def get(self,request,*args,**kwargs):

        res = {
            'name':'sanzid',
            'age' : 24,
        }
        return render(request,'post.html',{'res':res})


class Login(View):
    def get(self,request,*args,**kwargs):
        frm = LoginForm()
        return render(request,'login.html',{'form':frm})
    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password =form.cleaned_data['pasword']
            username = email.split('@')[0]+email.split('@')[1].split('.')[0]
            user = authenticate(request, username=username, password=password)
            print(username,password,user)
            if user is not None:
                login(request, user)
                return redirect(to='/')
        return render(request,'login.html',{'form':form})


class Register(View):
    def get(self,request,*args,**kwargs):
        frm = RegisterForm()
        return render(request,'register.html',{'form':frm})
    def post(self,request,*args,**kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            # password = form.cleaned_data['pasword']
            username =email.split('@')[0]+email.split('@')[1].split('.')[0]
            obj = form.save(commit=False)
            obj.username = username
            obj.save()
            return redirect(to='/')
        return render(request,'register.html',{'form':form})

def logout_user(request,*arg,**kwarg):
    logout(request)
    return redirect('login/')
