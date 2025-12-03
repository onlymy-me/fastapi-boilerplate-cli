import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ui"
    debug: bool = True
    api_v1_str: str = "/api/v1"
    
    class Config:
        env_file = ".env"


settings = Settings()
