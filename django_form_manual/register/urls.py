from django.urls import path
from .views import register_view,Login,Register
urlpatterns = [
    path('', register_view,name='test'),
    path('register/', Register.as_view(),name='register'),
    path('login/', Login.as_view(),name='login'),

]
