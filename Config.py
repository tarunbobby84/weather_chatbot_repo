import os
from dotenv import load_dotenv

load_dotenv()

class DefaultConfig:
    OPENAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    OPENAI_ENGINE = os.getenv("AZURE_OPENAI_ENGINE")
    OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
