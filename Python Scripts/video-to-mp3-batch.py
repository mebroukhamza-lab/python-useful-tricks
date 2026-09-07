# pip install moviepy
import os
from moviepy.editor import VideoFileClip
for file in os.listdir("videos"):
    if file.endswith(".mp4"):
        clip = VideoFileClip(f"videos/{file}")
        clip.audio.write_audiofile(f"videos/{file.replace('.mp4', '.mp3')}")
        clip.close()
print("All videos converted to mp3 successfully")
