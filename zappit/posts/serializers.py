from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source = 'poster = serializers.ReadOnlyField(source = .username')
    poster = serializers.ReadOnlyField(source = 'poster.id')
    class Meta:
        model = Post
        fields = ['id','title','url','poster','poster_id','created']