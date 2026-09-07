# pip install subprocess (built-in, no install needed) - Windows only
import subprocess
data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8", errors="ignore")
profiles = [line.split(":")[1].strip() for line in data.split("\n") if "All User Profile" in line]
for profile in profiles:
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8", errors="ignore")
        password_line = [l for l in result.split("\n") if "Key Content" in l]
        password = password_line[0].split(":")[1].strip() if password_line else "N/A"
        print(f"{profile}: {password}")
    except subprocess.CalledProcessError:
        continue
