```python
import smtplib
from email.message import EmailMessage
from twilio.rest import Client

# Email credentials
EMAIL_ADDRESS = "you@example.com"
EMAIL_PASSWORD = "yourpassword"

# Twilio credentials
TWILIO_SID = "your_twilio_sid"
TWILIO_TOKEN = "your_twilio_auth_token"
TWILIO_FROM = "+1234567890"

NGO_CONTACTS = ["ngo1@example.com", "ngo2@example.com"]
POLICE_EMAIL = "police@emergency.gov"
HOSPITAL_EMAIL = "hospital@emergency.gov"


def send_email(subject, body, to_list):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = ", ".join(to_list)
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


def send_sms(body, to_phone):
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    client.messages.create(body=body, from_=TWILIO_FROM, to=to_phone)


def notify_all(data):
    location = data.get("location", "Unknown")
    incident_type = data.get("type", "Incident")
    message = f"⚠️ {incident_type} reported at {location}. Immediate assistance required."

    # Send to emergency services
    send_email(f"{incident_type} Alert", message, [POLICE_EMAIL, HOSPITAL_EMAIL] + NGO_CONTACTS)

    # Optional: Send SMS to relative (if phone passed)
    if 'relative_phone' in data:
        send_sms(message, data['relative_phone'])
```

