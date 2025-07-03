# backend/config.py

import os
from dotenv import load_dotenv
from pydantic import BaseSettings, Field

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    # Project Info
    PROJECT_NAME: str = "Sustainable Smart City Assistant"
    API_VERSION: str = "v1"

    # IBM Watsonx Granite LLM
    GRANITE_API_KEY: str = Field(..., env="GRANITE_API_KEY")

    # Pinecone Vector Database
    PINECONE_API_KEY: str = Field(..., env="PINECONE_API_KEY")
    PINECONE_ENV: str = Field(..., env="PINECONE_ENV")
    PINECONE_INDEX_NAME: str = Field("smartcity-index", env="PINECONE_INDEX_NAME")

    # Logging & Debugging
    LOG_LEVEL: str = Field("info", env="LOG_LEVEL")
    DEBUG_MODE: bool = Field(False, env="DEBUG_MODE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create a single shared settings instance
settings = Settings()
