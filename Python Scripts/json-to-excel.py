# pip install pandas openpyxl
import pandas as pd
import json
with open("data.json") as f:
    data = json.load(f)
df = pd.DataFrame(data)
df.to_excel("data.xlsx", index=False)
print("JSON converted to Excel successfully")
