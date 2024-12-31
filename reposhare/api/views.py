from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from .utils.github_api import GitHubAPI
from django.http import JsonResponse

def fetch_repo_info(request):
    token = "nuh uh"  # Ideally, load from environment variables
    github = GitHubAPI(token)
    
    # Example input
    owner = "django"
    repo_name = "django"
    
    data = github.get_repo_info(owner, repo_name)
    return JsonResponse(data)

