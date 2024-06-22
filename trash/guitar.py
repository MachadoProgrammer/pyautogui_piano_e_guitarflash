import pyautogui
from time import sleep
import keyboard

sleep(1)

# def click(x, y):
#    win32api.SetCursorPos((x, y))
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#    time.sleep(0.05)
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(723, 895)[0] == 255:
        pyautogui.press('l')
        sleep(0.05)
    elif pyautogui.pixel(617, 897)[0] == 255:
        pyautogui.press('k')
        sleep(0.05)
    elif pyautogui.pixel(507, 897)[0] == 255:
        pyautogui.press('j')
        sleep(0.05)

    elif pyautogui.pixel(403, 895)[0] == 255:
        pyautogui.press('s')
        sleep(0.05)
    elif pyautogui.pixel(298, 896)[0] == 255:
        pyautogui.press('a')
        sleep(0.05)
