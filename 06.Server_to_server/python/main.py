from fastapi import FastAPI
from datetime import datetime
import requests

app = FastAPI()


@app.get("/date")
def get_date():
    return datetime.now()

@app.get("/datefromexpress")
def get_date():
    response = requests.get("http://127.0.0.1:8080/Date")
    return response.json()

@app.get("/datefrom_mikkel")
def get_date():
    response = requests.get("https://440d-195-249-146-100.eu.ngrok.io/date")
    return response.json()