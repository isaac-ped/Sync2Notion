import pytest
from unittest.mock import MagicMock
from source2notion.github_client import GitHubClient


@pytest.fixture
def github_client():
    client = GitHubClient(token="dummy_token")
    client.fetch_repo_structure = MagicMock(return_value={"folders": [], "files": []})
    client.fetch_readme = MagicMock(return_value="# Example README")
    return client


def test_fetch_repo_structure(github_client):
    repo_name = "example/repo"
    structure = github_client.fetch_repo_structure(repo_name)
    assert isinstance(structure, dict)
    assert "folders" in structure
    assert "files" in structure


def test_fetch_readme(github_client):
    repo_name = "example/repo"
    readme_content = github_client.fetch_readme(repo_name)
    assert isinstance(readme_content, str)
    assert len(readme_content) > 0
    assert readme_content.startswith("#")
