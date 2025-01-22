from github import Github
import os
import sys

# Retrieve the GitHub token from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set.")
    sys.exit(1)

def bulk_repo_visibility_change(repos_to_change, new_visibility='private'):
    try:
        g = Github(GITHUB_TOKEN)
        user = g.get_user()
        print(f"Authenticated as: {user.login}")
    except Exception as e:
        print(f"Error during authentication: {e}")
        return []

    changed_repos = []
    for repo_name in repos_to_change:
        try:
            repo = user.get_repo(repo_name)
            repo.edit(private=(new_visibility.lower() == 'private'))
            changed_repos.append(repo_name)
            print(f"Changed '{repo_name}' to {new_visibility}")
        except Exception as e:
            print(f"Error changing '{repo_name}': {e}")

    return changed_repos

# Example usage
if __name__ == "__main__":
    repos = [
        'Name-Repo',
    ]
    bulk_repo_visibility_change(repos)