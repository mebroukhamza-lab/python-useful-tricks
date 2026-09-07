# pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
url = "https://example.com"
soup = BeautifulSoup(requests.get(url).text, "html.parser")
for i, img in enumerate(soup.find_all("img")):
    src = img.get("src")
    if src and src.startswith("http"):
        data = requests.get(src).content
        with open(f"image_{i}.jpg", "wb") as f:
            f.write(data)
print("Images downloaded successfully")
