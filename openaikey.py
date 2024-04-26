from dotenv import load_dotenv

import os

load_dotenv()

def get_open_eg_ai_key() -> str:
    return os.getenv("EG_OPENAI_API_KEY")

def get_open_bloomtech_key() -> str:
    return os.getenv("BT_OPENAI_API_KEY")

def get_openai_key():
    return get_open_bloomtech_key()
