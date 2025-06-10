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

class ReposView(APIView):
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
        repo_owner = request.query_params.get('repo_owner', None)
        if repo_name is None or repo_name is None:
            return Response(status=400)
        data = github.get_repo_issues(repo_owner, repo_name)
        return Response(data)


    
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
        success = response.get('state') == state
        return Response(response, status=200 if success else 500)

class RepoInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        github = GithubAPI(request.user)
        repo_name = request.query_params.get('repo_name', None)
        repo_owner = request.query_params.get('repo_owner', None)
        
        if not repo_name or not repo_owner:
            return Response(
                {"error": "Both repo_owner and repo_name parameters are required"},
                status=400
            )
        
        try:
            data = github.get_repo(f"{repo_owner}/{repo_name}")
            return Response(data)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=500
            )

class CreateIssueView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        owner = request.data.get('owner')
        repo = request.data.get('repo')
        title = request.data.get('title')
        body = request.data.get('body', '')

        if not owner or not repo or not title:
            return Response({"error": "owner, repo, and title are required"}, status=400)

        github = GithubAPI(request.user)
        result = github.create_issue(owner, repo, title, body)
        if "id" in result:
            return Response(result, status=201)
        return Response(result, status=400)

