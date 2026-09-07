# pip install moviepy
from moviepy.editor import VideoFileClip
clip = VideoFileClip("video.mp4")
clip.audio.write_audiofile("audio.mp3")
clip.close()
print("Audio extracted successfully")
