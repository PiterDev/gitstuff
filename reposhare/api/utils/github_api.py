import requests

class GitHubAPI:
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token):
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_repo_info(self, owner, repo_name):
        url = f"{self.BASE_URL}/repos/{owner}/{repo_name}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "name": data.get("name"),
                "description": data.get("description"),
                "icon": data.get("owner", {}).get("avatar_url"),
                "issues": data.get("open_issues_count"),
                "last_commit": data.get("pushed_at")
            }
        else:
            return {"error": response.json().get("message", "Failed to fetch repo info.")}

