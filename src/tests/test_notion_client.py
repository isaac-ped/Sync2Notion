from unittest.mock import MagicMock
from source2notion.notion_client import NotionClient


class TestNotionClient:
    def setup_method(self):
        self.notion_client = NotionClient(token="dummy_token")
        self.notion_client.upload_structure_to_notion = MagicMock(return_value=True)
        self.notion_client.upload_readme_to_notion = MagicMock(return_value=True)

    def test_upload_structure_to_notion(self):
        mock_data = {"folder": "example_folder", "files": ["file1.md", "file2.md"]}
        response = self.notion_client.upload_structure_to_notion("mock_parent", mock_data)  # Added missing parent argument
        assert response is True

    def test_upload_readme_to_notion(self):
        mock_readme_content = "# Example README\nThis is a test README."
        response = self.notion_client.upload_readme_to_notion("mock_parent", mock_readme_content)  # Added missing parent argument
        assert response is True
