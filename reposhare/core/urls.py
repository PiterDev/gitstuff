from django.urls import path
from . import views

urlpatterns = [
    path("repo/<str:owner>/<str:repo>", views.repo, name="repo"),
    path("login/", views.github_login, name="login"),
    path("", views.main_page, name="main_page"),
    path("toggle_upvote/<str:repo_owner>/<str:repo_name>", views.toggle_upvote, name="toggle_upvote"),
]
