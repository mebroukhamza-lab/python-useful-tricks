# pip install deep-translator
from deep_translator import GoogleTranslator
text = "Hello, how are you?"
translated = GoogleTranslator(source="auto", target="fr").translate(text)
print("Translated text:", translated)
