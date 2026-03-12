from dotenv import load_dotenv
import os

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

required_vars = [
    "GITHUB_TOKEN",
    "GITHUB_WEBHOOK_SECRET",
    "GOOGLE_API_KEY",
    "LANGCHAIN_API_KEY"
]

missing = [var for var in required_vars if not os.getenv(var)]
if missing:
    raise ValueError(f"Missing environment variables: {missing}")

print("✅ All environment variables loaded successfully")

