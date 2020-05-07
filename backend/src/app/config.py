import secrets
from typing import List

from pydantic import BaseSettings, AnyHttpUrl

class Settings(BaseSettings):
    PROJECT_NAME: str = "E-learn tracker API"
    API_V1_STR: str = "/elearntracker/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://192.168.56.1", "https://192.168.56.1", "http://localhost", "http://localhost:8080"]

    class Config:
        case_sensitive = True

settings = Settings()
