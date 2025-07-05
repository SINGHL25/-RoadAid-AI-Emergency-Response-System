```python
import streamlit as st
import folium
from streamlit_folium import st_folium
import json

st.set_page_config(page_title="Responder Map", layout="wide")
st.title("📍 Responder Assignment Map")

m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

with open("data/sample_incident.json") as f:
    incident = json.load(f)
    lat, lon = map(float, incident['location'].split(", "))
    folium.Marker([lat, lon], tooltip="🚨 Incident Location").add_to(m)

st_folium(m, width=700, height=500)
```
