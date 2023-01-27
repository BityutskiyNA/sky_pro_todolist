import os
from pydantic import BaseSettings

class Settings_TDL(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DJ_SECRET_KEY: str
    DJ_DEBUG: bool
    DATABASE_URL: str
    class Config:
        case_sensitive = True
        env_file = ".env"