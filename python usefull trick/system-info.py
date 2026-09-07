# pip install psutil
import psutil
print("CPU usage:", psutil.cpu_percent(), "%")
print("RAM usage:", psutil.virtual_memory().percent, "%")
print("Disk usage:", psutil.disk_usage("/").percent, "%")
