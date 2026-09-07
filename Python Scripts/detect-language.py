# pip install langdetect
from langdetect import detect
text = "Bonjour tout le monde"
lang = detect(text)
print("Detected language:", lang)
