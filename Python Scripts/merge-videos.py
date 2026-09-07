# pip install moviepy
from moviepy.editor import VideoFileClip, concatenate_videoclips
clip1 = VideoFileClip("video1.mp4")
clip2 = VideoFileClip("video2.mp4")
final = concatenate_videoclips([clip1, clip2])
final.write_videofile("merged.mp4")
print("Videos merged successfully")
