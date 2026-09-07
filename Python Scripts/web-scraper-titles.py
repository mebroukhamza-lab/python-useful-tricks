# pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
response = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("span", class_="titleline")
for t in titles[:10]:
    print(t.text)
print("Titles scraped successfully")
