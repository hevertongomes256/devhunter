import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """

    API_V1_STR: str = '/api/v1'

    DB_URL: str = os.getenv('DB_URL')

    JWT_SECRET: str = os.getenv('JWT_SECRET')

    ALGORITHM: str = os.getenv('ALGORITHM')

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1

    class Config:
        case_sensitive = True


settings = Settings()
