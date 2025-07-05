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
