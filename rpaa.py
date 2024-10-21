'''
import pyautogui

print(pyautogui.size())
#1600(w) and 900(h)

print(pyautogui.position()) #mouse cursor position
#moveto() and click()

#move the cursor to specified coordinate
#pyautogui.moveTo(1400,300,1)

pyautogui.moveRel(-498,996, duration = 1)
 
# clicks at the present location
pyautogui.click() 
 
# moves to the specified location
pyautogui.moveTo(1165,637, duration = 1)
 
# right clicks at the present cursor
# location
pyautogui.click(button="right") 
 
# moves to the specified location
pyautogui.moveTo(1207,621, duration = 1)
 
# clicks at the present location
pyautogui.click()




'''

# used to access time related functions
'''
import time 
 
# pauses the execution of the program 
# for 5 sec
time.sleep(5) 
 
# types the string passed inside the 
# function
pyautogui.typewrite("RPA!") 
'''

