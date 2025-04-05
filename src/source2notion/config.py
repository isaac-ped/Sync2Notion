import os
from dotenv import load_dotenv
from pathlib import Path
from dataclasses import dataclass
from typing import ClassVar, Self


@dataclass
class Config:
    """Configuration object to hold environment variables."""

    GITHUB_TOKEN: str
    NOTION_TOKEN: str
    NOTION_DATABASE_ID: str | None = None  # Made optional

    _instance: ClassVar[Self | None] = None

    @classmethod
    def Get(cls) -> Self:
        if cls._instance is None:
            dotenv_path: Path = Path(__file__).resolve().parent.parent.parent / ".env"
            load_dotenv(dotenv_path)
            cls._instance = cls(
                GITHUB_TOKEN=os.getenv("GITHUB_TOKEN", ""),
                NOTION_TOKEN=os.getenv("NOTION_TOKEN", ""),
                NOTION_DATABASE_ID=os.getenv("NOTION_DATABASE_ID"),  # Optional
            )

            # Validate that required variables are set
            if not cls._instance.GITHUB_TOKEN:
                raise ValueError(
                    "GITHUB_TOKEN is not set in the environment variables."
                )
            if not cls._instance.NOTION_TOKEN:
                raise ValueError(
                    "NOTION_TOKEN is not set in the environment variables."
                )
        return cls._instance
