from fastapi import FastAPI
from pydantic import BaseModel
import json

listOfEventTypes = ["item.created", "item.updated", "item.removed"]

ITEM_REMOVED_EVENT_TYPE = "item.removed"
ITEM_CREATED_EVENT_TYPE = "item.created"
ITEM_UPDATED_EVENT_TYPE = "item.updated"



app = FastAPI()

class Item(BaseModel):
    id: int 
    name: str
    price: float

class Webhook(BaseModel):
    url: str
    eventType: str

    def __eq__(self, other):
        if not isinstance(other, Webhook):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.url == other.url and self.eventType == other.eventType
    def __hash__(self):
        return hash((self.url, self.eventType))

db = []
webhooks = set()

@app.get("/items")
async def read_items():
    return db

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    return {"message": "Item not found"}

@app.post("/items")
async def create_item(item: Item):
    db.append(item)
    sendEventToWebhooks(ITEM_CREATED_EVENT_TYPE,item)
    return {"message": "Item created"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    for i in range(len(db)):
        if db[i].id == item_id:
            db[i] = item
            sendEventToWebhooks(ITEM_UPDATED_EVENT_TYPE,item)
            return {"message": "Item updated"}
    return {"message": "Item not found"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for item in db:
        if item.id == item_id:
            itemDeleted = item
            del item
            sendEventToWebhooks(ITEM_REMOVED_EVENT_TYPE,itemDeleted)
            return {"message": "Item deleted"}
    return {"message": "Item not found"}
@app.get("/webhooks")
async def getwebhooks():
    return webhooks

@app.post("/addwebhook")
async def addwebhook(webhook : Webhook):
    if webhook.eventType not in listOfEventTypes:
        return {"message": "Event type not allowed"}

    statuscode = pingWebhook(webhook)
    if not str(statuscode).startswith("20"):
        return {"message": "Failed to ping. Statuscode: " + statuscode }
    
    webhooks.add(webhook)
    
    return {"message": "Webhook added successfully"}


import requests
def pingWebhook(webhook : Webhook):
    data = {
            'type': webhook.eventType,
            'object': "ping"}
    try:
        response = requests.post(webhook.url, json=data)
        return response.status_code
    except requests.exceptions.RequestException as e:
            print(f"Failed to ping {webhook}. Exception: {e}")
            return 500

def sendEventToWebhooks(eventType, object):
    try:
        for webhook in webhooks:
            if not eventType == webhook.eventType:
                continue
            requests.post(webhook.url, json={"type": webhook.eventType, "object": object.dict()}) 
    except:
        pass

