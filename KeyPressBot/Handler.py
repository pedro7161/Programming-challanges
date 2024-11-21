import time
import pyautogui
import keyboard

def PressKeyTimes(key, times=10, interval=0.1,start_time = 0,stop_key='q'):
    time.sleep(start_time)
    for _ in range(times):
        pyautogui.press(key)
        if keyboard.is_pressed(stop_key):
            print("You pressed", stop_key, "to stop the key presses.")
            return
        time.sleep(interval)
