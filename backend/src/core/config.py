from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SmartFlow AI"
    api_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./smartflow.db"
    jwt_secret: str = "change-me"
    jwt_refresh_secret: str = "change-refresh-me"
    client_url: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
