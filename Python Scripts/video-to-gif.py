# pip install moviepy
from moviepy.editor import VideoFileClip
clip = VideoFileClip("video.mp4")
clip.write_gif("output.gif")
clip.close()
print("GIF saved successfully")
