from django.urls import path
from . import views

urlpatterns = [
    path("repo/<str:owner>/<str:repo>", views.repo, name="repo"),
    path("login/", views.github_login, name="login"),
    path("", views.main_page, name="main_page"),
]
