from pydantic_settings import BaseSettings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):

    database_host: str
    database_port: str
    database_user: str
    database_pass: str
    database_name: str

    debug: bool = False

    class Config:
        env_file = os.path.join(BASE_DIR, ".env")
        env_file_encoding = 'utf-8'

settings = Settings()
