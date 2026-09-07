# pip install pyspellchecker
from spellchecker import SpellChecker
spell = SpellChecker()
text = "helo wrld this is a tst"
misspelled = spell.unknown(text.split())
for word in misspelled:
    print(word, "->", spell.correction(word))
