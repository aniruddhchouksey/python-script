
import time 
import pyautogui 
while True:
    time.sleep(30)
    pyautogui.moveRel(10, 0, duration = .05) 
    pyautogui.moveRel(0, 5, duration = .05) 
    pyautogui.moveRel(-10, 0, duration = .05) 
    pyautogui.moveRel(0, -5, duration = .05) 
    pyautogui.hotkey("altleft", "tab") 


