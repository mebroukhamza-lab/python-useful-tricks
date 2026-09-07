# pip install pandas openpyxl
import pandas as pd
import glob
files = glob.glob("excel_files/*.xlsx")
merged = pd.concat([pd.read_excel(f) for f in files])
merged.to_excel("merged.xlsx", index=False)
print("Excel files merged successfully")
