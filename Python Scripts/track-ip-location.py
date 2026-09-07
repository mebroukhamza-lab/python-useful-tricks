# pip install requests
import requests
ip = "8.8.8.8"
response = requests.get(f"https://ipinfo.io/{ip}/json")
print(response.json())
