from django.shortcuts import render
from allauth.socialaccount.models import SocialToken
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect

from .models import Repo, Upvote
from .forms import ChooseRepoForm

import requests


def get_repo_info(owner, repo, token):
    github_api_url = f'https://api.github.com/repos/{owner}/{repo}'
    headers = {'Authorization': f'token {token}'}
    print(token)

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

    # upvoted = Upvote.objects.filter(repo__owner=owner, repo__name=repo, user=request.user).exists()
    repo_obj, created = Repo.objects.get_or_create(owner=owner, name=repo)
    is_upvoted = Upvote.objects.filter(user=request.user, repo=repo_obj).exists()
    print(repo_obj.name) # false should be true
    upvotes = repo_obj.upvote_set.count()


    if repo_info:
        return render(request, 'repo_card.html', {'repo_info': repo_info, 'upvoted': is_upvoted, 'upvotes': upvotes})
    else:
        return render(request, 'error.html', {'error': 'Failed to fetch repository information.'})

def main_page(request):
    return render(request, 'main_page.html', {'user': request.user})

def github_login(request):
    return render(request, 'github_login.html')

@login_required
def toggle_upvote(request, repo_owner, repo_name):
    repo, _ = Repo.objects.get_or_create(owner=repo_owner, name=repo_name)
    upvote, created = Upvote.objects.get_or_create(user=request.user, repo=repo)
    print(repo_owner, repo_name)

    if not created:
        upvote.delete()
        # remove vote from repo
        upvote_amount = repo.upvote_set.count()
        return JsonResponse({'status': 'downvoted', 'upvotes': upvote_amount})
    else:
        upvote_amount = repo.upvote_set.count()
        return JsonResponse({'status': 'upvoted', 'upvotes': upvote_amount})

def goto_repo_form(request):
    if request.method == 'POST':
        form = ChooseRepoForm(request.POST)
        if form.is_valid():
            return redirect('repo', form.cleaned_data['owner'], form.cleaned_data['name'])
    else:
        form = ChooseRepoForm()
    return render(request, 'choose_repo.html', {'form': form})