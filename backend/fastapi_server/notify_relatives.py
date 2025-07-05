```python
import smtplib
from email.mime.text import MIMEText
import json

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASS = 'your_app_password'

def send_email_alert(subject, message, to_email):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASS)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

with open("data/relatives.json") as f:
    relatives = json.load(f)
    for relative in relatives:
        send_email_alert(
            "🚨 Accident Alert",
            "An accident has been reported near your contact. Please check in immediately.",
            relative['email']
        )
```
