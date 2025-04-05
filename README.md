# GitHub to Notion Sync Application

This project provides a tool to synchronize the folder structure and README files of a GitHub repository to a Notion workspace. It leverages the GitHub API to fetch repository details and the Notion API to upload the data.

## Features

- Fetches the folder structure of a specified GitHub repository.
- Retrieves the README file content from the repository.
- Syncs the fetched data to a Notion workspace.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/source2notion.git
   cd source2notion
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To sync a GitHub repository to Notion, you can use the `SyncService` class. Here’s a basic example:

```python
from source2notion.sync_service import SyncService

repo_name = "yourusername/yourrepository"
sync_service = SyncService()
sync_service.sync_repo_to_notion(repo_name)
```

## Configuration

Create a `.env` file in the root directory with the following content:

```
GITHUB_TOKEN=your_github_token
NOTION_TOKEN=your_notion_token
NOTION_DATABASE_ID=your_notion_database_id
```

## Creating a Notion API Token

To use the Notion integration, you need to create a Notion API token. Follow these steps:

1. Go to the [Notion Developers Page](https://www.notion.so/my-integrations).
2. Click on the "+ New Integration" button.
3. Fill in the required details for your integration:
   - **Name**: Provide a name for your integration (e.g., "Source2Notion Integration").
   - **Associated Workspace**: Select the workspace where you want to use this integration.
4. Click "Submit" to create the integration.
5. Copy the "Internal Integration Token" provided. This is your Notion API token.

### Setting the Token in Your Environment

1. Open your terminal and navigate to the project directory.
2. Create a `.env` file in the root of the project if it doesn't already exist.
3. Add the following line to the `.env` file, replacing `your_token_here` with your actual Notion API token:

   ```env
   NOTION_TOKEN=your_token_here
   ```

4. Save the file. The application will automatically load this token when running.

## Running Tests

To run the tests for this project, use the following command:

```
pytest src/tests
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.