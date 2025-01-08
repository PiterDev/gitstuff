from django.shortcuts import render
from allauth.socialaccount.models import SocialToken
from django.contrib.auth.decorators import login_required
import requests

def get_repo_info(owner, repo, token):
    github_api_url = f'https://api.github.com/repos/{owner}/{repo}'
    headers = {'Authorization': f'token {token}'}

    response = requests.get(github_api_url, headers=headers)

    if response.status_code != 200:
        raise Exception(f'Failed to fetch GitHub API for {owner}/{repo}:\n{response.text}')
    
    return response.json()

def get_github_token(user):
    try:
        token = SocialToken.objects.get(account=user.socialaccount_set.get(provider='github'))
        return token.token
    except SocialToken.DoesNotExist:
        return None

@login_required
def repo(request, owner, repo):
    token = get_github_token(request.user)
    if not token:
        return render(request, 'error.html', {'error': 'You need to login with GitHub to view this page.'})
    
    repo_info = get_repo_info(owner, repo, token)

    if repo_info:
        return render(request, 'repo_card.html', {'repo_info': repo_info})
    else:
        return render(request, 'error.html', {'error': 'Failed to fetch repository information.'})

def main_page(request):
    
    return render(request, 'main_page.html', {'user': request.user})

def github_login(request):
    return render(request, 'github_login.html')