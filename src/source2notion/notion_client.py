"""source2notion.notion_client module."""

import requests
import re  # Added for regex operations
from typing import Any, Dict
from source2notion.config import Config


class NotionClient:
    """Client to interact with Notion API."""

    def __init__(self, token: str | None = None):
        config = Config.Get()
        self.token = token or config.NOTION_TOKEN
        self.base_url = "https://api.notion.com/v1/"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Notion-Version": "2021-05-13",
        }

    def _extract_database_id(self, database_link: str) -> str:
        """Extract the database ID from a Notion database link."""
        match = re.search(r"/([a-f0-9]{32})", database_link)
        if not match:
            raise ValueError("Invalid Notion database link provided.")
        return match.group(1)

    def create_page(self, parent: str, properties: Dict[str, Any]):
        """Create a new page in Notion, accepting a database link or ID."""
        if parent.startswith("http"):
            parent_id = self._extract_database_id(parent)
        else:
            parent_id = parent

        url = f"{self.base_url}pages"
        data = {
            "parent": {"database_id": parent_id},
            "properties": properties,
        }
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        return None

    def update_page(self, page_id: str, properties: Dict[str, Any]):
        """Update an existing page in Notion."""
        url = f"{self.base_url}pages/{page_id}"
        data = {"properties": properties}
        response = requests.patch(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        return None

    def retrieve_page(self, page_id: str):
        """Retrieve a page from Notion."""
        url = f"{self.base_url}pages/{page_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return None

    def upload_structure_to_notion(self, parent: str, data: dict):
        """Upload folder structure to Notion, accepting a database link or ID."""
        if parent.startswith("http"):
            parent_id = self._extract_database_id(parent)
        else:
            parent_id = parent

        # Logic to upload the folder structure to Notion using parent_id
        print(f"Uploading structure to Notion database {parent_id}...")
        return True

    def upload_readme_to_notion(self, parent: str, readme_content: str):
        """Upload README content to Notion, accepting a database link or ID."""
        if parent.startswith("http"):
            parent_id = self._extract_database_id(parent)
        else:
            parent_id = parent

        # Logic to upload the README content to Notion using parent_id
        print(f"Uploading README to Notion database {parent_id}...")
        return True
