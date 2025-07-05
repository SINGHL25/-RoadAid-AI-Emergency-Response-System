```python
from fastapi import FastAPI, Request
from pydantic import BaseModel
import datetime

app = FastAPI()

class Incident(BaseModel):
    location: str
    description: str
    time: str

@app.get("/")
def read_root():
    return {"message": "RoadAid AI Backend Running"}

@app.post("/report")
def report_incident(incident: Incident):
    print(f"New incident at {incident.location}: {incident.description}")
    return {"status": "success", "timestamp": datetime.datetime.now().isoformat()}



```python
from fastapi import FastAPI, Request
from firebase_config import db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"msg": "RoadAid API live"}

@app.post("/submit")
def submit_report(data: dict):
    db.collection('incidents').add(data)
    return {"status": "Saved"}
```
```

