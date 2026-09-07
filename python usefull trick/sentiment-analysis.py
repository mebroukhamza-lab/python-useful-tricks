# pip install textblob
from textblob import TextBlob
text = "I really love this new phone, it's amazing!"
blob = TextBlob(text)
print("Sentiment polarity:", blob.sentiment.polarity)
