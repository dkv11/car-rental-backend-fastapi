from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.core.config import settings



print(settings.app_name)

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "OK"}