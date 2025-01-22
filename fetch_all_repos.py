from github import Github
import os
import sys

def get_public_repos(username):
    # Retrieve the GitHub token from environment variables
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable not set.")
        sys.exit(1)
    
    try:
        # Authenticate with GitHub
        g = Github(GITHUB_TOKEN)
        user = g.get_user(username)
        print(f"Authenticated as: {g.get_user().login}")
    except Exception as e:
        print(f"Error during authentication or fetching user: {e}")
        sys.exit(1)
    
    try:
        # Fetch all public repositories
        public_repos = user.get_repos(type='public')
        
        print(f"\nPublic Repositories for {username}:")
        print("-" * 40)
        for repo in public_repos:
            print(repo.name)
    except Exception as e:
        print(f"Error fetching repositories: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Replace 'target_username' with the GitHub username you want to query
    target_username = 'Grundrak'  # e.g., 'octocat'
    
    get_public_repos(target_username)