import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)  

db_path = os.path.join(PROJECT_DIR, "tasks.db")
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{db_path}")
