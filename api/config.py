from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
CLE_SECRETE=os.getenv("CLE_SECRETE")
CLE_METEO=os.getenv("CLE_METEO")

print(DB_NAME)