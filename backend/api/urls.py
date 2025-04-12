from django.urls import path, include
from dj_rest_auth.views import LoginView, LogoutView
from .views import TestView, UserInfoView, RepoIssuesView, IssueUpdateView

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('user', UserInfoView.as_view(), name='user'),
    path('repo_issues', RepoIssuesView.as_view(), name='repo_issues'),
    path('update_issue', IssueUpdateView.as_view(), name="issue_update")
]