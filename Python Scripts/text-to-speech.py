# pip install gTTS
from gtts import gTTS
text = "hello"
tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")
print("audio saved succesfully")
