# pip install moviepy
from moviepy.editor import VideoFileClip
clip = VideoFileClip("video.mp4")
clip.write_videofile("compressed.mp4", bitrate="500k")
clip.close()
print("Video compressed successfully")
