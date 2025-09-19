from pydantic_settings import BaseSettings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):

    # Database
    database_host: str
    database_port: int
    database_user: str
    database_pass: str
    database_name: str

    # Application
    debug: bool = False
    log_level: str = 'INFO'

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')
        env_file_encoding = 'utf-8'

    @property
    def database_url(self: object) -> str:
        return f'postgresql+asyncpg://{self.database_user}:{self.database_pass}@{self.database_host}:{self.database_port}/{self.database_name}'

settings = Settings()
