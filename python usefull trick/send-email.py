# pip install secure-smtplib (built-in smtplib, no install needed)
import smtplib
from email.mime.text import MIMEText
msg = MIMEText("Hello, this is an automated email.")
msg["Subject"] = "Test Email"
msg["From"] = "you@gmail.com"
msg["To"] = "friend@gmail.com"
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("you@gmail.com", "your_app_password")
    server.send_message(msg)
print("Email sent successfully")
