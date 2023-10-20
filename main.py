import subprocess
import time

subprocess.run(["nircmd.exe", "setprimarydisplay", r"\\.\DISPLAY3"])
subprocess.run(["nircmd.exe", "setdefaultsounddevice", "Philips FTV"])
subprocess.run(["nircmd.exe", "setsysvolume", "65535"])
steam_process = subprocess.Popen(["C:\\Gry\\Steam\\steam.exe", "-gamepadui"])

while True:
    if steam_process.poll() is not None:
        break
    time.sleep(1)
    
subprocess.run(["nircmd.exe", "setprimarydisplay", r"\\.\DISPLAY2"])
subprocess.run(["nircmd.exe", "setdefaultsounddevice", "Głośniki", "1"])
subprocess.run(["nircmd.exe", "setsysvolume", "65535"])

