### 📁 dashboard/app.py
```python
import streamlit as st
import pandas as pd
import pydeck as pdk
import firebase_admin
from firebase_admin import credentials, firestore
import time

st.set_page_config(layout="wide")
st.title("🗺️ RoadAid Live Incident Map")

cred = credentials.Certificate("../fastapi_server/firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@st.cache_data(ttl=30)
def load_data():
    docs = db.collection("incidents").stream()
    return [doc.to_dict() for doc in docs]

# Auto-refresh every 30 seconds
st_autorefresh = st.empty()
while True:
    st_autorefresh.empty()
    data = load_data()
    df = pd.DataFrame(data)

    if not df.empty:
        # Filters
        types = df['type'].unique().tolist()
        selected_types = st.multiselect("Filter by type:", types, default=types)

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        min_time, max_time = df['timestamp'].min(), df['timestamp'].max()
        selected_range = st.slider("Select time range:", min_value=min_time, max_value=max_time, value=(min_time, max_time))

        # Apply filters
        df = df[df['type'].isin(selected_types)]
        df = df[(df['timestamp'] >= selected_range[0]) & (df['timestamp'] <= selected_range[1])]

        # Show map
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/streets-v11',
            initial_view_state=pdk.ViewState(
                latitude=df['latitude'].mean(),
                longitude=df['longitude'].mean(),
                zoom=10,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df,
                    get_position='[longitude, latitude]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=100,
                ),
            ],
        ))

        st.dataframe(df)
    else:
        st.warning("No incidents reported yet.")

    time.sleep(30)
```
