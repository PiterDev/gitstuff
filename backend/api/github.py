import requests
from allauth.socialaccount.models import SocialToken

class GithubAPI:
    def __init__(self, user):
        self.token = self.get_github_token(user)
        if not self.token:
            raise Exception('No token found')
        self.headers = {
            'Authorization': f'token {self.token}',
            "Accept": "application/vnd.github.v3+json"
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
        url = f'{self.base_url}/repos/{owner}/{repo_name}/issues?state=all'
        response = requests.get(url, headers=self.headers)
        all_json = response.json()

        only_issues = [issue for issue in all_json if "pull_request" not in issue]


        return only_issues 
    
    def close_issue(self, owner, repo_name, issue_number):
        url = f'{self.base_url}/repos/{owner}/{repo_name}/issues/{issue_number}'
        body = {
            "state": "closed"
        }
        response = requests.patch(url, json=body, headers=self.headers)
        return response.json()
    
    def open_issue(self, owner, repo_name, issue_number):
        url = f'{self.base_url}/repos/{owner}/{repo_name}/issues/{issue_number}'
        body = {
            "state": "open"
        }
        response = requests.patch(url, json=body, headers=self.headers)
        return response.json()

    def create_issue(self, owner, repo_name, title, body=""):
        url = f'{self.base_url}/repos/{owner}/{repo_name}/issues'
        payload = {
            "title": title,
            "body": body
        }
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()