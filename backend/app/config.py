from pydantic_settings import BaseSettings
from dotenv import load_dotenv

#TODO: load_dotenv()

class Settings(BaseSettings):
    class Config:
        env_file = ".env"