# pip install moviepy
from moviepy.editor import VideoFileClip
clip = VideoFileClip("video.mp4").subclip(10, 30)
clip.write_videofile("trimmed.mp4")
print("Video trimmed successfully")
