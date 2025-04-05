"""
source2notion.github_client
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module provides a client to interact with the GitHub API.
"""

import requests
from source2notion.config import Config


class GitHubClient:
    """Client to interact with GitHub API."""

    def __init__(self, token: str | None = None):
        config = Config.Get()
        self.token = token or config.GITHUB_TOKEN
        self.base_url = "https://api.github.com"

    def _headers(self):
        return {"Authorization": f"token {self.token}"}

    def get_user(self):
        """Fetch authenticated user information."""
        url = f"{self.base_url}/user"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def get_repos(self):
        """Fetch repositories of the authenticated user."""
        url = f"{self.base_url}/user/repos"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def fetch_repo_structure(self, repo_name: str):
        """Fetch the folder structure of a repository."""
        url = f"{self.base_url}/repos/{repo_name}/contents"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def fetch_readme(self, repo_name: str):
        """Fetch the README file of a repository."""
        url = f"{self.base_url}/repos/{repo_name}/readme"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json().get("content", "")
