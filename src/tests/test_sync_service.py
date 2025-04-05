import pytest
from source2notion.sync_service import SyncService
from source2notion.github_client import GitHubClient
from source2notion.notion_client import NotionClient


class MockGitHubClient(GitHubClient):
    def __init__(self, token=None):  # Accept and ignore the token argument
        pass

    def fetch_repo_structure(self, repo_name: str):
        return {"folder1": {}, "folder2": {"subfolder": {}}}

    def fetch_readme(self, repo_name: str):
        return "This is a README file."

    def get_repos(self):
        return [{"name": "repo1"}, {"name": "repo2"}]  # Mocked repo list


class MockNotionClient(NotionClient):
    def __init__(self, token=None):  # Accept and ignore the token argument
        pass

    def upload_structure_to_notion(self, parent: str, data: dict):
        return True

    def upload_readme_to_notion(self, parent: str, readme_content: str):
        return True

    def create_page(self, parent: str, properties: dict):
        return {"id": "mock_page_id"}  # Mocked response


@pytest.fixture
def sync_service(monkeypatch):
    monkeypatch.setattr("source2notion.sync_service.GitHubClient", MockGitHubClient)
    monkeypatch.setattr("source2notion.sync_service.NotionClient", MockNotionClient)
    return SyncService()


def test_sync_repo_to_notion(sync_service):
    result = sync_service.sync_repo_to_notion("test-repo")
    assert result is True


def test_sync(sync_service):
    sync_service.sync()  # Ensure no exceptions are raised
