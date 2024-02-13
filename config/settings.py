import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

DEBUG = bool(os.environ.get("DEBUG"))

DB_USER = os.environ.get("DB_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOSTNAME = os.environ.get("DB_HOSTNAME")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}"

app = FastAPI(debug=DEBUG)
