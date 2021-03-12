from django.shortcuts import render
# Create your views here.
from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework import mixins,generics
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class StudentDetail(mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)