from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DATABASE_URL: str

    REDIS_HOST: str
    REDIS_PORT: int

    QDRANT_HOST: str
    QDRANT_PORT: int

    JWT_SECRET_KEY: str

    LLM_API_BASE: str
    LLM_API_KEY: str
    LLM_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()