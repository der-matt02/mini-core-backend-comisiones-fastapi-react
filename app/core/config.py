from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # /home/dermattubu/CoreBackend

class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    @property
    def sqlalchemy_database_url(self):
        return (
            f"mysql+pymysql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    class Config:
        env_file = BASE_DIR / ".env"
        env_prefix = ""  # Esto permite usar nombres directos como DB_HOST
        case_sensitive = False

settings = Settings()
