import os
from dotenv import load_dotenv
import click
from source2notion.github_client import GitHubClient
from source2notion.notion_client import NotionClient

# Load environment variables from .env file
load_dotenv()


def sync_github_to_notion(repo: str, database: str, token: str):
    """Sync a GitHub repository to Notion."""
    github_client = GitHubClient(token=token)
    notion_client = NotionClient()

    # Fetch repository structure and README from GitHub
    repo_structure = github_client.fetch_repo_structure(repo)
    readme_content = github_client.fetch_readme(repo)

    # Upload data to Notion
    notion_client.upload_structure_to_notion(database, repo_structure)
    notion_client.upload_readme_to_notion(database, readme_content)


@click.group()
def s2n():
    """Source2Notion CLI."""
    pass


@s2n.command()
@click.option(
    "--repo", required=True, help="GitHub repository to sync from (e.g., owner/repo)."
)
@click.option(
    "--database", required=True, help="Notion database link or ID to sync to."
)
def github(repo: str, database: str):
    """Sync from GitHub to Notion."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN is not set in the environment variables.")

    sync_github_to_notion(repo, database, token)


if __name__ == "__main__":
    s2n()
