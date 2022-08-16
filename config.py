from pydantic import BaseSettings


class Settings(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str

    class Config:
        env_file = 'env/.env'
