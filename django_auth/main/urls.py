from unicodedata import name
from django.urls import path
from .views import Home,Login,Register,logout_user
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(Home.as_view(),login_url='/login'),name='home'),
    path('login/',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),
    path('logout',logout_user,name='logout')
]