from github import Github
import config

# First create a Github instance using an access token
g = Github(config.GITHUB_TOKEN)

def create_plan(issue):
    # TODO: Implement logic for creating a plan this should use the prompt and call open ai api
    
    print(f"Creating a plan for issue {issue.number}")
