from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Python Boilerplate"
    app_version: str = "0.1.0"
    app_description: str = "A FastAPI boilerplate application"
    debug: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
