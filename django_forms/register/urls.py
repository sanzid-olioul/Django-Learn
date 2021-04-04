from unicodedata import name
from django.urls import path
from .views import Login,Register
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login'),name='login'),
    path('register/', Register.as_view(),name='register'),
    path('login/', Login.as_view(),name='login'),

]
