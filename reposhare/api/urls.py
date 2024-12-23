from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostListCreate.as_view(), name="post-view-create"),
    path("posts/<int:pk>/", views.PostRetrieveUpdateDestroy.as_view(), name="update"),
    path('fetch-repo-info/', views.fetch_repo_info, name='fetch_repo_info'),
]