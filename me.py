
import time 
import pyautogui 
while True:
    time.sleep(1)   
    pyautogui.moveRel(1000, 0, duration = 5) 
    pyautogui.moveRel(0, 500, duration = 5) 
    pyautogui.moveRel(-1000, 0, duration = 5) 
    pyautogui.moveRel(0, -500, duration = 5) 


