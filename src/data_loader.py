"""Data loading utilities for the sports match outcome prediction project."""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "database.sqlite"


def get_database_path() -> Path:
    return DB_PATH
