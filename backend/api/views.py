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
        return Response(data, status=data.get('status', 200))

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

# class CloseIssueView(APIView):
#     permission_classes = [IsAuthenticated]

#     def patch(self, request, owner, repo, id):
#         github = GithubAPI(request.user)
#         github.close_issue(owner, repo, id)
#         return Response(status=200)

# class OpenIssueView(APIView):
#     permission_classes = [IsAuthenticated]

#     def patch(self, request, owner, repo, id):
#         github = GithubAPI(request.user)
#         github.open_issue(owner, repo, id)
#         return Response(status=200)
    
class IssueUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        owner = request.data.get('owner')
        repo = request.data.get('repo')
        id = request.data.get('id')
        state = request.data.get('state')

        github = GithubAPI(request.user)
        success = False
        if state == 'open':
             response = github.open_issue(owner, repo, id)
        else:
            response = github.close_issue(owner, repo, id)
        return Response(response, status=200 if success else 500)