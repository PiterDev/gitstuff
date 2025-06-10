from django.shortcuts import render
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from .custom_oauth_client import CustomGitHubOAuth2Client

class GithubLoginView(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "http://localhost:5173/auth/github/callback" # https://gitstuff.piterdev.me/auth/github/callback"
    client_class = CustomGitHubOAuth2Client
