# pip install requests
import requests
sites = ["https://google.com", "https://github.com", "https://openai.com"]
for site in sites:
    try:
        r = requests.get(site, timeout=5)
        print(site, "->", r.status_code)
    except requests.RequestException:
        print(site, "-> DOWN")
