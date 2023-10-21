import pygetwindow as gw
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


list = []

for curr_win in gw.getAllTitles():
    window = gw.getWindowsWithTitle(curr_win)[0]
    if window.title == '':
        pass
    else:
        list.append([window.title, window.left, window.top, window.width, window.height, window.isMinimized])
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

for win in list:
    window = gw.getWindowsWithTitle(win[0])[0]
    window.restore()
    if win[5] == "True":
        window.minimize()
    window.left = win[1]
    window.top = win[2]
    window.width = win[3]
    window.height = win[4]