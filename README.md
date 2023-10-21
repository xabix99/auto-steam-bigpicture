# Automated Steam Big Picture Mode Switcher

This Python script is designed to automate the process of switching to Steam's Big Picture Mode for a seamless gaming experience on a dedicated display with customized audio settings.

## Dependencies

- **Python**

- **PyInstaller**

- **PyGetWindow**

## Configuration

Edit `main.py` to fit your needs:

- **STEAM_PATH**: Path to your Steam executable `steam.exe`.

- **DISPLAY_STEAM**: The display you want to use for Steam's Big Picture Mode. This should be specified as a numeric value corresponding to the desired display.

- **DISPLAY_MAIN**: The display you want to use for everything else. Also specified as a numeric value.

- **VOLUME_STEAM**: The desired volume level for Steam in percentage.

- **VOLUME_MAIN**: The desired volume level for all other applications in percentage.

- **AUDIO_SOURCE_STEAM**: The audio source you want to use for Steam.

- **AUDIO_SOURCE_MAIN**: The audio source you want to use for all other applications.

## How to run
Assuming that you have python and pyinstaller already installed and you configured `main.py`:

1.Run create_exe.py.

2.Add generated `AutomatedBigPicture.exe` file to your taskbar or wherever you want and run it.

## How the Script Works

The script performs the following steps:

1. Gets all current windows position

2. Turns on Bluetooth (using the PowerShell script).

3. Sets the primary display to the one specified for Steam.

4. Sets the default sound device to the one specified for Steam.

5. Adjusts the system volume to the desired level for Steam.

6. Launches Steam in Big Picture Mode.

7. Monitors the Steam process and waits until it exits.

8. Restores the primary display to the original one.

9. Resets the default sound device and system volume to their initial settings.

10. Turns off Bluetooth.

11. Restores all windows state

## Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. Feel free to modify and distribute the code as per the terms of the license.
