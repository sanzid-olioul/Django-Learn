
from django.urls import path,include
from .views import StudentList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student',StudentList)




urlpatterns = [
    path('',include(router.urls)),
]
