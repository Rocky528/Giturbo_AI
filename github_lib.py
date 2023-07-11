import requests
import re

def get_github_links_from_issue_content(issue_content):
    github_links = re.findall(r'(?:https?://)?github\.com/[\w\-]+/[\w\-]+', issue_content)
    return github_links
    
def get_github_file_content(owner, repo, path):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url)
    response_json = response.json()

    if 'content' in response_json:
        content = response_json['content']
        decoded_content = content.decode('base64')  # Decode base64 content
        return decoded_content
    else:
        return None