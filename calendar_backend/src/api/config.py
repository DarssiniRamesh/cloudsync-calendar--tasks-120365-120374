import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# PUBLIC_INTERFACE
class Settings:
    """App configuration from environment variables for DB connection etc."""

    DB_HOST: str = os.getenv("POSTGRES_URL", "localhost")
    DB_USER: str = os.getenv("POSTGRES_USER", "calendaruser")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "calendarpass")
    DB_NAME: str = os.getenv("POSTGRES_DB", "calendardb")
    DB_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    DB_ASYNC_URL: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Any other common config (for further extension)


settings = Settings()
