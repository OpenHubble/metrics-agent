# Pydantic Settings
import tomllib
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# Settings Class
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # App
    app_mode: str = ""

    # Server
    allowed_ips: str = ""

    # Agent
    bind_ip: str = "0.0.0.0"
    port: int = 9703

    # Host
    hostname: str = ""

    # API
    api_key: str = ""

    # Data from pyproject.toml
    project_name: str = ""
    project_version: str = ""
    project_description: str = ""
    project_authors: list[str] = Field(default_factory=list)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        pyproject = Path(__file__).resolve().parent.parent / "pyproject.toml"

        if pyproject.exists():
            with pyproject.open("rb") as f:
                data = tomllib.load(f)

            metadata = data.get("tool", {}).get("openhubble", {})

            self.project_name = metadata.get("name", "")
            self.project_version = metadata.get("version", "")
            self.project_description = metadata.get("description", "")
            self.project_authors = metadata.get("authors", [])


# Run settings
settings = Settings()
