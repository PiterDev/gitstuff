from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
# from dj_rest_auth.registration.serializers import SocialLoginSerializer
from .custom_serializers import SocialLoginSerializer
from allauth.socialaccount.models import SocialToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import RepoNameSerializer
import requests



class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "http://localhost:5173/auth/github/callback/"
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

class GithubRepoInfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_github_token(self, user):
        try:
            token = SocialToken.objects.get(account__user=user, account__provider='github')
            print("TOKEN " + token.token)
            return token.token
        except SocialToken.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        serializer = RepoNameSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        token = self.get_github_token(request.user)
        if not token:
            return Response({"error": "No GitHub token found for user"}, status=400)

        repo_name = request.query_params.get('repo_name')
        repo_owner = request.query_params.get('repo_owner')
        if not repo_name:
            return Response({"error": "Repository name is required"}, status=400)

        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
        }
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return Response(response.json(), status=response.status_code)

        return Response(response.json(), status=200)
