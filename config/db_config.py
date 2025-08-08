from dotenv import load_dotenv
import os

load_dotenv()

settings = {
    "host": os.getenv("FSTR_DB_HOST", "localhost"),
    "port": os.getenv("FSTR_DB_PORT", "5432"),
    "database": os.getenv("FSTR_DB_NAME", "pereval"),
    "user": os.getenv("FSTR_DB_LOGIN", "postgres"),
    "password": os.getenv("FSTR_DB_PASS", "postgres")
}