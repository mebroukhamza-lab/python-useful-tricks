# pip install requests
import requests
response = requests.get("https://api.quotable.io/random")
quote = response.json()
print(f'"{quote["content"]}" - {quote["author"]}')
