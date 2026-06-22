"""
Standalone helper functions for system control, web actions, and volume.
Not currently wired into core.py (which has its own inline versions of
some of this) - kept here as reusable utilities / for future use.
"""

import os
import platform
import webbrowser
import urllib.parse

try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    VOLUME_AVAILABLE = True
except ImportError:
    VOLUME_AVAILABLE = False


# --- System controls ---

def lock_computer():
    try:
        system = platform.system()

        if system == "Windows":
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif system == "Linux":
            os.system("loginctl lock-session")
        elif system == "Darwin":
            os.system(
                "/System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -suspend"
            )
    except Exception as e:
        print(f"Lock error: {e}")


def shutdown_computer():
    try:
        system = platform.system()

        if system == "Windows":
            os.system("shutdown /s /t 0")
        elif system == "Linux":
            os.system("shutdown now")
        elif system == "Darwin":
            os.system("sudo shutdown -h now")
    except Exception as e:
        print(f"Shutdown error: {e}")


def restart_computer():
    try:
        system = platform.system()

        if system == "Windows":
            os.system("shutdown /r /t 0")
        elif system == "Linux":
            os.system("reboot")
        elif system == "Darwin":
            os.system("sudo reboot")
    except Exception as e:
        print(f"Restart error: {e}")


def sleep_computer():
    try:
        system = platform.system()

        if system == "Windows":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif system == "Linux":
            os.system("systemctl suspend")
        elif system == "Darwin":
            os.system("pmset sleepnow")
    except Exception as e:
        print(f"Sleep error: {e}")


# --- Web actions ---

def open_google():
    webbrowser.open("https://www.google.com")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def search_google(query):
    query = urllib.parse.quote(query)
    webbrowser.open(f"https://www.google.com/search?q={query}")


def search_youtube(query):
    query = urllib.parse.quote(query)
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


# --- Volume control (Windows only) ---

def get_volume_interface():
    if not VOLUME_AVAILABLE:
        return None

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume))


def set_volume(percent):
    if not VOLUME_AVAILABLE:
        return

    try:
        percent = max(0, min(100, percent))
        volume = get_volume_interface()
        volume.SetMasterVolumeLevelScalar(percent / 100, None)
    except Exception as e:
        print(f"Volume error: {e}")


def mute_volume():
    if not VOLUME_AVAILABLE:
        return

    try:
        get_volume_interface().SetMute(1, None)
    except Exception as e:
        print(f"Mute error: {e}")


def unmute_volume():
    if not VOLUME_AVAILABLE:
        return

    try:
        get_volume_interface().SetMute(0, None)
    except Exception as e:
        print(f"Unmute error: {e}")


def volume_up():
    if not VOLUME_AVAILABLE:
        return

    try:
        volume = get_volume_interface()
        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)
    except Exception as e:
        print(f"Volume up error: {e}")


def volume_down():
    if not VOLUME_AVAILABLE:
        return

    try:
        volume = get_volume_interface()
        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)
    except Exception as e:
        print(f"Volume down error: {e}")
