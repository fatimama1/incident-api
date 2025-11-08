import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", 8000))

    DB_USER: str = os.getenv("POSTGRES_USER", "postgres")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    DB_HOST: str = os.getenv("DB_HOST", "db")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("POSTGRES_DB", "incidents_db")

    @property
    def DATABASE_URL(self) -> str:
        """URL основной БД для приложения"""
        return (
            f"postgresql+asyncpg://{self.DB_USER}:"
            f"{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
