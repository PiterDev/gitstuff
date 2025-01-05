from django.urls import path
from . import views

urlpatterns = [
    path("repo/<str:owner>/<str:repo>", views.repo, name="repo"),
]
