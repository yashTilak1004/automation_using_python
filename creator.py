import time
import pyautogui

#go the Drive D
pyautogui.press('win')
pyautogui.typewrite('file')
pyautogui.press('enter')
time.sleep(1)
locate = pyautogui.locateOnScreen('image.png',confidence=0.9)
center = pyautogui.center(locate)
pyautogui.doubleClick(center)
time.sleep(1)
pyautogui.press('right')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(1)

#now in Drive D->go to folder->go to object->hotkey
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('up')
pyautogui.press('enter')
time.sleep(1)
#pyautogui.press('tab')
#pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.hotkey('ctrl','c')
time.sleep(1)
pyautogui.press('backspace')
time.sleep(1)
#create a new folder
pyautogui.hotkey('ctrl','shift','n')
pyautogui.typewrite('New Folder 2')
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl','v')