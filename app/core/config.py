from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import SecretStr, computed_field



class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


    @computed_field
    @property
    def db_url(self) -> str:
        return (f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD.get_secret_value()}'
                f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}')
    



settings = Settings()



    