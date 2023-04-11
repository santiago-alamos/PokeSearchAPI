import os

PRODUCTION = os.environ.get("PRODUCTION", False) == "True"
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "")
DOCS_URL = os.getenv("DOCS", "/docs")
