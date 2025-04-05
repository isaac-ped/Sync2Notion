import pytest
from unittest.mock import patch
from source2notion.config import Config


@pytest.fixture(autouse=True)
def mock_env_vars():
    """Mock environment variables for all tests."""
    with patch.dict(
        "os.environ",
        {
            "GITHUB_TOKEN": "mock_github_token",
            "NOTION_TOKEN": "mock_notion_token",
            "NOTION_DATABASE_ID": "mock_notion_database_id",
        },
    ):
        # Clear the singleton instance to ensure fresh initialization
        Config._instance = None
        yield
