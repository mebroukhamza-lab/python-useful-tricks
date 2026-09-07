# pip install spotdl
import subprocess
url = "https://open.spotify.com/track/xxxxxxxx"
subprocess.run(["spotdl", url])
print("Track downloaded successfully")
