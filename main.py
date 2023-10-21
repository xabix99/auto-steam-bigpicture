import subprocess
import time
import os

STEAM_PATH = "C:\\Gry\\Steam\\steam.exe"
DISPLAY_STEAM = 3
DISPLAY_MAIN = 2
VOLUME_STEAM = 100
VOLUME_MAIN = 100
AUDIO_SOURCE_STEAM = "Philips FTV"
AUDIO_SOURCE_MAIN = "Głośniki"

vol_steam = int(VOLUME_STEAM * 65535 / 100)
vol_main = int(VOLUME_MAIN * 65535 / 100)
display_steam_value = r"\\.\DISPLAY" + str(DISPLAY_STEAM)
display_main_value = r"\\.\DISPLAY" + str(DISPLAY_MAIN)

subprocess.run(["DisableBluetooth.exe"])
subprocess.run(["EnableBluetooth.exe"])
subprocess.run(["nircmd.exe", "setprimarydisplay", f"{display_steam_value}"])
subprocess.run(["nircmd.exe", "setdefaultsounddevice", f"{AUDIO_SOURCE_STEAM}","1"])
subprocess.run(["nircmd.exe", "setsysvolume", f"{vol_steam}"])
steam_process = subprocess.Popen([f"{STEAM_PATH}", "-gamepadui"])

while True:
    if steam_process.poll() is not None:
        break
    time.sleep(1)
    
subprocess.run(["nircmd.exe", "setprimarydisplay", f"{display_main_value}"])
subprocess.run(["nircmd.exe", "setdefaultsounddevice", f"{AUDIO_SOURCE_MAIN}", "1"])
subprocess.run(["nircmd.exe", "setsysvolume", f"{vol_main}"])
subprocess.run(["DisableBluetooth.exe"])