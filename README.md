# RoadAid AI

Emergency Response System for Road Accidents
roadaid-ai/
├── mobile_app/                # Flutter app (UI + GPS + sensors)
├── backend/
│   ├── fastapi_server/        # Alert API endpoints, blood lookup
│   └── firebase_config.py     # Firebase admin init
├── dashboard/                 # Streamlit dashboard for NGO, authority
├── ml_models/                 # YOLOv8 for crash detection or OCR
├── data/                      # Sample logs, mock APIs
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ✨ Core Features

| Feature                      | Description |
|-----------------------------|-------------|
| 🚗 Crash Detection           | From mobile sensors or dashcam AI (YOLO) |
| 📍 Live Location Sharing     | Shares to hospital, police, family |
| 📞 Emergency Call/SMS        | Auto-notifies registered contacts |
| 🩸 Blood Request System      | Integrates with APIs like eRaktKosh |
| 🐾 Animal Aid Reporting      | Notifies animal rescue units or RSPCA |
| 💰 NGO Fund Request          | Pings local NGO dashboard |
| 📊 Analytics + Heatmaps      | Live stats for accidents, locations |

---

## ✅ Social Impact
- Fast aid delivery in human/animal road crashes
- Connects families and resources
- Prevents roadside deaths
- Can be used by Governments, Smart Cities, NGOs

---

## 📜 Standards for Reliability & Usability

- ✅ **12-Factor App** guidelines for deployment
- ✅ RESTful API with schema validation
- ✅ Firebase Auth + Push Notification Standards
- ✅ UI/UX Guidelines for accessibility and multilingual (EN/HI)
- ✅ Streamlit for rapid, friendly dashboards
- ✅ End-to-end logging, alerts, fallback in case of internet loss

---

## ▶️ Getting Started

```bash
# Install backend deps
pip install -r requirements.txt

# Run Streamlit dashboard
streamlit run dashboard/app.py

# Start FastAPI backend
uvicorn backend.fastapi_server.main:app --reload
```

---
