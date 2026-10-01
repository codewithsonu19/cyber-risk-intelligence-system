import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


APP_NAME = os.getenv(
    "APP_NAME",
    "CyRIQ"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "1.0.0"
)

DEBUG = os.getenv(
    "DEBUG",
    "True"
).lower() == "true"


DATABASE_PATH = BASE_DIR / os.getenv(
    "DATABASE_PATH",
    "database/cyriq.db"
)

MODEL_PATH = BASE_DIR / os.getenv(
    "MODEL_PATH",
    "ml/model.pkl"
)

DATA_PATH = BASE_DIR / "data"

ML_DATA_PATH = BASE_DIR / "ml" / "data"