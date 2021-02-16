from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import generics,permissions
# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(poster=self.request.user)
