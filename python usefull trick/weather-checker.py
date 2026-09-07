# pip install requests
import requests
city = "Casablanca"
url = f"https://wttr.in/{city}?format=3"
response = requests.get(url)
print(response.text)
