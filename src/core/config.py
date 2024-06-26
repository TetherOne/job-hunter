from pydantic import BaseModel, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class EmailConfig(BaseModel):
    host: str
    port: str
    user: str
    password: str
    use_ssl: bool


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    resumes: str = "/resumes"
    contacts: str = "/contacts"
    vacancies: str = "/vacancies"
    email: str = "/email"
    favorites: str = "/favorites"
    users: str = "/users"


class RedisConfig(BaseSettings):
    url: str = "envs/redis.env"
    port: int = "envs/redis.env"
    db: int = "envs/redis.env"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class S3Config(BaseModel):
    access_key: SecretStr
    secret_key: SecretStr
    endpoint_url: str
    bucket_name: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="envs/.env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FAST_API_HH__",
        arbitrary_types_allowed=True,
    )
    api: ApiPrefix = ApiPrefix()
    s3: S3Config
    db: DatabaseConfig
    email: EmailConfig
    cache: RedisConfig


settings = Settings()
