from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        Post.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    lookup_field = "pk"

