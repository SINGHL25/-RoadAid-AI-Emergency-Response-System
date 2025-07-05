```python
from fastapi import APIRouter
import requests
import json

router = APIRouter()

@router.get("/ngos")
def get_ngos():
    with open("data/ngos.json") as f:
        return json.load(f)

@router.get("/hospitals")
def get_hospitals():
    with open("data/hospitals.json") as f:
        return json.load(f)

@router.get("/police")
def get_police():
    with open("data/police_stations.json") as f:
        return json.load(f)
```
