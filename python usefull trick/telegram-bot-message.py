# pip install python-telegram-bot
import requests
token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
message = "Hello from my Python bot!"
url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
requests.get(url)
print("Telegram message sent successfully")
