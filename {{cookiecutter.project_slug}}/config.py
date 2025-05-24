# {{cookiecutter.project_slug}}/src/{{cookiecutter.project_slug}}/config.py
"""
Configuration management for {{ cookiecutter.project_name }}.

This module defines the application settings, loading them from environment
variables and .env files using Pydantic-settings.
"""

from typing import Literal, Optional

from pydantic import AnyHttpUrl, Field, PostgresDsn, RedisDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.

    These settings are loaded from environment variables and/or an .env file.
    Refer to .env.example for a list of all possible environment variables.
    """

    # --- General Project Configuration ---
    # These are typically set by Cookiecutter and can be overridden by .env if needed.
    APP_NAME: str = Field(default="{{ cookiecutter.project_name }}")
    DESCRIPTION: str = Field(default="{{ cookiecutter.description }}")
    VERSION: str = Field(default="{{ cookiecutter.version }}")  # From cookiecutter.json

    # Environment mode and logging level, configurable via .env
    PYTHON_ENV: Literal["development", "staging", "production", "testing"] = Field(
        default="development"
    )
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO"
    )

    # --- API Keys & Service Credentials (Loaded from .env if present) ---
    # All fields for external services are Optional. Their presence in the .env file
    # is guided by the conditionally templated .env.example.
    # Application logic should check if these optional settings are None before use.

    # OpenAI
    OPENAI_API_KEY: Optional[SecretStr] = Field(default=None)
    OPENAI_ORG_ID: Optional[str] = Field(default=None)

    # Google (Gemini / Vertex AI)
    GOOGLE_API_KEY: Optional[SecretStr] = Field(
        default=None
    )  # For Gemini Studio API Key
    # GOOGLE_APPLICATION_CREDENTIALS often set as an OS environment variable directly
    # pointing to the service account JSON file path for Vertex AI.
    # Pydantic-settings will pick it up if it's set in the environment.
    GOOGLE_APPLICATION_CREDENTIALS: Optional[str] = Field(default=None)

    # Ollama
    OLLAMA_HOST: Optional[AnyHttpUrl] = Field(
        default=None
    )  # e.g., "http://localhost:11434"

    # LangChain
    LANGCHAIN_TRACING_V2: Optional[str] = Field(
        default=None
    )  # Typically "true" or "false"
    LANGCHAIN_API_KEY: Optional[SecretStr] = Field(default=None)  # For LangSmith
    LANGCHAIN_PROJECT: Optional[str] = Field(
        default=None
    )  # For LangSmith, can default to APP_NAME

    # Pinecone (if used with LangChain or directly)
    PINECONE_API_KEY: Optional[SecretStr] = Field(default=None)
    PINECONE_ENVIRONMENT: Optional[str] = Field(
        default=None
    )  # e.g., "gcp-starter", "us-west1-gcp"

    # Database (Example for PostgreSQL)
    # Prefer setting DATABASE_URL directly in .env for most drivers.
    # Individual components are provided for flexibility if needed.
    DB_TYPE: Optional[str] = Field(
        default=None, description="Type of database e.g., postgresql, mysql, sqlite"
    )
    DB_HOST: Optional[str] = Field(default=None)
    DB_PORT: Optional[int] = Field(default=None)
    DB_USER: Optional[str] = Field(default=None)
    DB_PASSWORD: Optional[SecretStr] = Field(default=None)
    DB_NAME: Optional[str] = Field(default=None)
    # For SQLAlchemy, a full DATABASE_URL is typically used.
    # Pydantic can validate it if type hinted with e.g., PostgresDsn.
    DATABASE_URL: Optional[str] = Field(
        default=None, description="Full database connection string"
    )
    # Example: For Postgres, you could use:
    # DATABASE_URL: Optional[PostgresDsn] = Field(default=None)

    # Redis
    # Prefer setting REDIS_URL directly in .env for most drivers.
    REDIS_HOST: Optional[str] = Field(default="localhost")
    REDIS_PORT: Optional[int] = Field(default=6379)
    REDIS_PASSWORD: Optional[SecretStr] = Field(default=None)
    REDIS_DB: Optional[int] = Field(default=0)
    # Example: For validated Redis URL:
    # REDIS_URL: Optional[RedisDsn] = Field(default=None) # e.g., "redis://user:pass@host:port/0"

    # n8n
    N8N_BASE_URL: Optional[AnyHttpUrl] = Field(
        default=None
    )  # e.g., "http://localhost:5678"
    N8N_API_KEY: Optional[SecretStr] = Field(default=None)

    # --- Pydantic-settings model configuration ---
    model_config = SettingsConfigDict(
        env_file=".env",  # Load variables from .env file
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra variables in .env not defined here
        case_sensitive=False,  # Environment variable names are usually case-insensitive
    )


# Create a single, globally accessible instance of the settings.
# Other modules in your package can import it like
