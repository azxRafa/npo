from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )

    project_name: str = Field(default='Lol kek azaza', env="PROJECT_NAME")
    log_level: str = Field(default='INFO', env="LOG_LEVEL")


settings = Settings()
