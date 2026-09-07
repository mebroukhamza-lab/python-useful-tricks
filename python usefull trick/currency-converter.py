# pip install requests
import requests
amount, base, target = 100, "USD", "MAD"
response = requests.get(f"https://open.er-api.com/v6/latest/{base}")
rate = response.json()["rates"][target]
print(f"{amount} {base} = {amount * rate:.2f} {target}")
