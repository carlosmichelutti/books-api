from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from typing import Literal
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class DatabaseSettings(BaseSettings):

    # Database
    host: str
    port: int
    user: str
    password: str
    name: str
    
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, '.env'),
        env_file_encoding='utf-8',
        env_prefix='DATABASE_',
        extra='ignore',
    )

    @property
    def database_url(self: object) -> str:
        return f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'

class AppSettings(BaseSettings):

    # Application
    debug: bool
    log_level: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, '.env'),
        env_file_encoding='utf-8',
        env_prefix='APP_',
        extra='ignore',
    )

class Settings(BaseModel):

    # Configuration settings
    database: DatabaseSettings = DatabaseSettings()
    # Application settings
    app: AppSettings = AppSettings()

settings = Settings()
