from rest_framework import serializers
from .models import BlogsModel

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogsModel
        fields = ['title','author','date_created','content','comment']