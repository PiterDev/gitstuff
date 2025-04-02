from django.urls import path, include
from .views import GithubLoginView

urlpatterns = [
    path('login', GithubLoginView.as_view(), name='github_login')
]