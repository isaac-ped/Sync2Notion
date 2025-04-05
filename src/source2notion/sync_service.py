"""source2notion.sync_service module."""

from source2notion.github_client import GitHubClient
from source2notion.notion_client import NotionClient
from source2notion.config import Config


class SyncService:
    """Service to sync GitHub repository data to Notion."""

    def __init__(self):
        config = Config.Get()
        self.github_service = GitHubClient(config.GITHUB_TOKEN)
        self.notion_service = NotionClient(config.NOTION_TOKEN)

    def sync(self):
        """Sync GitHub repository data to Notion."""
        config = Config.Get()
        notion_database_id = config.NOTION_DATABASE_ID
        if not notion_database_id:
            raise ValueError(
                "NOTION_DATABASE_ID is not set in the environment variables."
            )

        repos = self.github_service.get_repos()
        for repo in repos:
            self.notion_service.create_page(
                parent=notion_database_id,  # Ensured type is str
                properties={"Name": {"title": [{"text": {"content": repo["name"]}}]}},
            )

    def sync_repo_to_notion(self, repo_name: str) -> bool:
        """Sync a specific GitHub repository to Notion."""
        config = Config.Get()
        notion_database_id = config.NOTION_DATABASE_ID
        if not notion_database_id:
            raise ValueError(
                "NOTION_DATABASE_ID is not set in the environment variables."
            )

        repo_structure = self.github_service.fetch_repo_structure(repo_name)
        readme_content = self.github_service.fetch_readme(repo_name)

        structure_uploaded = self.notion_service.upload_structure_to_notion(
            parent=notion_database_id,  # Ensured type is str
            data=repo_structure,
        )

        readme_uploaded = self.notion_service.upload_readme_to_notion(
            parent=notion_database_id,  # Ensured type is str
            readme_content=readme_content,
        )

        return structure_uploaded and readme_uploaded
