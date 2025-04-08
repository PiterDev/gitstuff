import requests
from allauth.socialaccount.models import SocialToken

class GithubAPI:
    def __init__(self, user):
        self.token = self.get_github_token(user)
        if not self.token:
            raise Exception('No token found')
        self.headers = {
            'Authorization': f'token {self.token}'
        }
        self.base_url = 'https://api.github.com'

    def get_github_token(self, user):
        try:
            token = SocialToken.objects.get(account=user.socialaccount_set.get(provider='github'))
            return token.token
        except SocialToken.DoesNotExist:
            return None

    def get_rate_limit(self):
        url = f'{self.base_url}/rate_limit'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_user(self):
        url = f'{self.base_url}/user'
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_repos(self):
        url = f'{self.base_url}/user/repos'
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_repo(self, repo_name):
        url = f'{self.base_url}/repos/{repo_name}'
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_repo_issues(self, owner, repo_name):
        url = f'{self.base_url}/repos/{owner}/{repo_name}/issues'
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def close_issue(self, owner, repo_name, issue_number):
        url = f'{self.base_url}/repos/{owner}/{repo_name}/issues/{issue_number}'
        body = {
            "state": "closed"
        }
        response = requests.patch(url, body, headers=self.headers)
        return response.status_code == 200
    
    def close_issue(self, owner, repo_name, issue_number):
        url = f'{self.base_url}/repos/{owner}/{repo_name}/issues/{issue_number}'
        body = {
            "state": "open"
        }
        response = requests.patch(url, body, headers=self.headers)
        return response.status_code == 200
