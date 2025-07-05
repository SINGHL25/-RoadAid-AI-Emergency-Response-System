```python
import streamlit as st
import json
import os

st.set_page_config(page_title="RoadAid Dashboard", layout="wide")
st.title("🛣️ RoadAid AI – Emergency Response Dashboard")

if os.path.exists("data/sample_incident.json"):
    with open("data/sample_incident.json") as f:
        incident = json.load(f)
    st.subheader("📍 Last Reported Incident")
    st.json(incident)
else:
    st.warning("No incidents found. Please report one via API.")

```python
import streamlit as st
import pandas as pd
import pydeck as pdk
import firebase_admin
from firebase_admin import credentials, firestore

st.set_page_config(layout="wide")
st.title("🗺️ RoadAid Live Incident Map")

cred = credentials.Certificate("../fastapi_server/firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Fetch incidents
docs = db.collection("incidents").stream()
data = [doc.to_dict() for doc in docs]
df = pd.DataFrame(data)

if not df.empty:
    st.map(df[['latitude', 'longitude']])
    st.write(df)
else:
    st.warning("No incidents reported yet.")
```

