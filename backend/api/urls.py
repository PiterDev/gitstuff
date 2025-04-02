from django.urls import path, include
from dj_rest_auth.views import LoginView, LogoutView
from .views import TestView, AdminView, UserInfoView

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path("test-admin/", AdminView.as_view(), name="test_admin"),
    path('test-user', UserInfoView.as_view(), name='test_user'),
]