from dj_rest_auth.views import LoginView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .github import GithubAPI

class TestView(APIView):
    def get(self, request):
        data = {'message': 'Hello, from the API!'}
        return Response(data)

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        github = GithubAPI(request.user)
        data = github.get_user()
        return Response(data)

class RepoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        github = GithubAPI(request.user)
        data = github.get_repos()
        return Response(data)
    

class RepoIssuesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        github = GithubAPI(request.user)
        repo_name = request.query_params.get('repo_name', None)
        if repo_name is None:
            return Response(status=400)
        data = github.get_repo_issues(request.user.username, repo_name)
        return Response(data)