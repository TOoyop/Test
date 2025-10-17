from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from typing import List, Optional
import secrets


class Settings(BaseSettings):
    app_name: str = "ThreadHub API"
    environment: str = "development"
    debug: bool = True

    # Security
    secret_key: str = secrets.token_urlsafe(32)
    access_token_expire_minutes: int = 60 * 24  # 1 day
    refresh_token_expire_minutes: int = 60 * 24 * 30  # 30 days
    algorithm: str = "HS256"

    # CORS
    backend_cors_origins: List[AnyHttpUrl] | List[str] = []

    # Database
    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/threadhub"

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # MeiliSearch
    meili_host: str = "http://localhost:7700"
    meili_api_key: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()