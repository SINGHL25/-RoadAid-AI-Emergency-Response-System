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
```

