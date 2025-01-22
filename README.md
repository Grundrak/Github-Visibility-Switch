# GitHub Repository Manager

A Python utility for managing GitHub repositories, including features to change repository visibility and fetch public repositories.

## Features

- Change repository visibility (public/private)
- Fetch all public repositories for a given username
- Bulk repository visibility changes
- Secure token-based authentication

## Prerequisites

- Python 3.6 or higher
- GitHub Personal Access Token

## Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd github-repo-manager
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

Windows:
```bash
.\venv\Scripts\activate
```

Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Generate a GitHub Personal Access Token:
   - Go to GitHub Settings > Developer Settings > Personal Access Tokens
   - Generate a new token with `repo` scope

2. Set the environment variable:

Windows:
```bash
setx GITHUB_TOKEN "your_github_token"
```

Unix/MacOS:
```bash
export GITHUB_TOKEN="your_github_token"
```

## Usage

### Change Repository Visibility

```python
python change_visibility_github.py
```

### Fetch Public Repositories

```python
python fetch_all_repos.py
```

## Example Code

```python
from github import Github
import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
g = Github(GITHUB_TOKEN)

# Change repository visibility
repos = ['repo-name-1', 'repo-name-2']
bulk_repo_visibility_change(repos, 'private')

# Fetch public repositories
get_public_repos('username')
```

## Project Structure

```
.
├── change_visibility_github.py    # Script for changing repo visibility
├── fetch_all_repos.py            # Script for fetching public repos
├── requirements.txt              # Project dependencies
├── .gitignore                    # Git ignore file
└── README.md                     # Project documentation
```

## Dependencies

- PyGithub
- requests
- python-dotenv

## Error Handling

The scripts include comprehensive error handling for:
- Missing GitHub tokens
- Authentication failures
- Repository access issues
- Network connectivity problems

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
