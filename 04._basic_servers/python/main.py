from typing import Union
import json
from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
import yaml
from yaml.loader  import SafeLoader
import csv 
import requests

app = FastAPI()
path = "../../02._data_formats/me"
 

with open(path + ".json" , 'r') as j:
    data = json.load(j)

@app.get("/")
def read_root():
    with open(path + ".json" , 'r') as j:
        data = json.load(j)
    return {"Me data":  data}


@app.get("/json")
def read_root():
    with open(path + ".json" , 'r') as j:
        data = json.load(j)
    return {"Me data":  data}

@app.get("/txt")
def read_root():
    with open(path + ".txt") as f: 
        data = f.readlines()
    return {"Me data":  data}

@app.get("/xml")
def read_root():
    with open(path + ".xml") as f:
        data = f.read()
    return {"Me data":  data}

@app.get("/yaml")
def read_root():
    with open(path + ".yaml") as f: 
        data = yaml.load(f,Loader=SafeLoader)
    return {"Me data":  data}

@app.get("/JsonFromNode")
def get_date():
    response = requests.get("http://localhost:8080/json")
    return response.json()
