from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
# from .utils.github_api import GitHubAPI
from allauth.socialaccount.models import SocialToken

from django.http import JsonResponse
from decouple import config
from django.contrib.auth.decorators import login_required
import requests

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

# def fetch_repo_info(request):
#     token = config("GH_PERSONAL_TOKEN")  # Ideally, load from environment variables
#     github = GitHubAPI(token)
    
#     # Example input
#     owner = "django"
#     repo_name = "django"
    
#     data = github.get_repo_info(owner, repo_name)
#     return JsonResponse(data)

@login_required
def github_proxy(request):
    github_api_url = "https://api.github.com/user/repos/django"


    # token = request.user.socialaccount_set.filter(provider='github')[0].socialtoken.token # Extract first oauth token

    try:
        token = SocialToken.objects.get(account__user=request.user, account__provider='github').token
    except SocialToken.DoesNotExist:
        return JsonResponse({"error": "GitHub token not found"}, status=403)

    headers = {"Authorization": f"token {token}"}
    response = requests.get(github_api_url, headers=headers)
    return JsonResponse(response.json(), safe=False)


