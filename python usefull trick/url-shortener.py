# pip install pyshorteners
import pyshorteners
s = pyshorteners.Shortener()
short_url = s.tinyurl.short("https://example.com/some/very/long/url")
print("Shortened URL:", short_url)
