
import time 
import pyautogui 
while True:
    time.sleep(1)   
    pyautogui.moveRel(1000, 100, duration = 1) 
    pyautogui.moveRel(-1000, 0, duration = 1) 

