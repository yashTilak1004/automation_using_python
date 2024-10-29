import time

import keyboard
import pyautogui


url = "https://ghcitrix.cloud.com"


def first_steps():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('go')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite('https://ghcitrix.cloud.com')
    pyautogui.press('enter')
    time.sleep(9)
    pyautogui.typewrite('Venkateshmn@gastrohealth.com')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite('Marshall$2025')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(9)
    locate = pyautogui.locateOnScreen('smol_chrome.png',confidence=0.8)
    center = pyautogui.center(locate)
    pyautogui.doubleClick(center)
    pyautogui.doubleClick(center)
    pyautogui.doubleClick(center)
    time.sleep(5)

import pyautogui
import keyboard
import time

def second_steps():
    pyautogui.press('win')
    pyautogui.write('file explorer', interval=0.1)  # Changed to write
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('down')
    pyautogui.press('right')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('down')
    pyautogui.press('up')
    pyautogui.press('enter')
    time.sleep(30)
    
    # Make sure the application is ready before sending keys
    time.sleep(6)
    keyboard.press("ctrl+a")
    keyboard.release("ctrl+a")
    time.sleep(2)
        
    keyboard.write("Venkateshmn@datamarshall.com")
    time.sleep(3)
    keyboard.press_and_release('tab')
    time.sleep(3)
        
        
    keyboard.write("Marshall$2025")
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')






first_steps()
second_steps()
exec(open('citrix_file_fetch.py').read())


'''
import pandas as pd
df = pd.read_excel('Locations.xlsx')
l = list(df['Sites'])
print(l)
cleaned_centers = [center[2:] if center.startswith('> ') else center for center in l]

# Print the cleaned list
print(cleaned_centers)
'''
#['LORTON ASC - Inova Ambulatory Surgery Center at LORTON', 'MSC - Inova McLean Surgery Center', 'NVSC - Inova Northern Virginia Surgery Center', 'PWASC - Prince William Ambulatory Surgery Center', 'RSC - RESTON SURGERY CENTER', 'SFASC - Inova Franconia Springfield Ambulatory Surgery Center', 'GHEGC - GHE Gastro Care', 'GHETSEC - GHE Tri State Endoscopy Center', 'FSC - Frederick Surgical Center', 'GDCB - Gastrointestinal Diagnostic Center of Baltimore', 'MDTEC - Maryland Diagnostic and Therapeutic Endo Center', 'GAEC - Gastroenterology Associates Endoscopy Center', 'GHE EDEC - GHE Edmonds Endoscopy Center', 'GHE EGEC - GHE Evergreen Endoscopy Center', 'GHE FEC - GHE Fremont Endoscopy Center', 'GHETCE - GHE Tri Cities Endoscopy Center PLLC', 'BMPSU - Baptist Medical Park Surgery Center', 'TECPEN - The Endoscopy Center of Pensacola', 'ADHEC - Alabama Digestive Health Endoscopy Center', 'GVEC - Grandview Endoscopy Center', 'OSE - Outpatient Services East', 'SASC - Shelby Ambulatory Surgery Center', 'AHSCCLM - AdventHealth Surgery Center Lake Mary', 'AHSCD - AdventHealth Surgery Center Davenport', 'ASC - Atlantic Surgery Center', 'AOC - Atlantis Outpatient Center', 'BAC - Bayside Ambulatory Center', 'BECCS - BHEC Coral Springs', 'CGE - BHEC Flagler', 'GEC - BHEC Galloway North', 'GSC - BHEC Galloway South', 'NPS - BHEC Northpoint', 'BHECPBG - BHEC Palm Beach Gardens', 'BHSFSH - BHEC South Palm', 'BROSLC - Boca Raton OP BROSLC', 'BROSC - Boca Raton OP Surgery and Laser Center', 'BSSC - Broward Specialty Surgical Center', 'CFSC - Central Florida Surgical Center', 'GCEC - Gulf Coast Endoscopy Center South', 'JOSC - Jupiter Outpatient Surgery Center', 'KESC - Kendall Endoscopy Surgery Center', 'KIEC - Kissimmee Endoscopy Center', 'KSC - Kissimmee Surgical Center', 'LSC - Laser and Surgery Center', 'OSS - Outpatient Surgical Services', 'PALMS W SC - Palms W Surgicenter', 'PSC - Parkcreek Surgery Center', 'SLSC - Sand Lake Surgery Center', 'SFSC - South Florida Surgical Center', 'SPSC - Summerport Surgery Center', 'SCCS - Surgery Center at Coral Springs', 'SCOA - Surgery Center Of Aventura', 'TOCBOY - The Outpatient Center of Boynton Beach', 'USC - University Surgery Center', 'VASC - Venture Ambulatory Surgical Center', 'WOSC - Weston Outpatient Surgical Center', 'SCFL - Surgery Center at Ft. Lauderdale']





l = ['LORTON ASC - Inova Ambulatory Surgery Center at LORTON', 'MSC - Inova McLean Surgery Center', 'NVSC - Inova Northern Virginia Surgery Center', 'PWASC - Prince William Ambulatory Surgery Center', 'RSC - RESTON SURGERY CENTER', 'SFASC - Inova Franconia Springfield Ambulatory Surgery Center', 'GHEGC - GHE Gastro Care', 'GHETSEC - GHE Tri State Endoscopy Center', 'FSC - Frederick Surgical Center', 'GDCB - Gastrointestinal Diagnostic Center of Baltimore', 'MDTEC - Maryland Diagnostic and Therapeutic Endo Center', 'GAEC - Gastroenterology Associates Endoscopy Center', 'GHE EDEC - GHE Edmonds Endoscopy Center', 'GHE EGEC - GHE Evergreen Endoscopy Center', 'GHE FEC - GHE Fremont Endoscopy Center', 'GHETCE - GHE Tri Cities Endoscopy Center PLLC', 'BMPSU - Baptist Medical Park Surgery Center', 'TECPEN - The Endoscopy Center of Pensacola', 'ADHEC - Alabama Digestive Health Endoscopy Center', 'GVEC - Grandview Endoscopy Center', 'OSE - Outpatient Services East', 'SASC - Shelby Ambulatory Surgery Center', 'AHSCCLM - AdventHealth Surgery Center Lake Mary', 'AHSCD - AdventHealth Surgery Center Davenport', 'ASC - Atlantic Surgery Center', 'AOC - Atlantis Outpatient Center', 'BAC - Bayside Ambulatory Center', 'BECCS - BHEC Coral Springs', 'CGE - BHEC Flagler', 'GEC - BHEC Galloway North', 'GSC - BHEC Galloway South', 'NPS - BHEC Northpoint', 'BHECPBG - BHEC Palm Beach Gardens', 'BHSFSH - BHEC South Palm', 'BROSLC - Boca Raton OP BROSLC', 'BROSC - Boca Raton OP Surgery and Laser Center', 'BSSC - Broward Specialty Surgical Center', 'CFSC - Central Florida Surgical Center', 'GCEC - Gulf Coast Endoscopy Center South', 'JOSC - Jupiter Outpatient Surgery Center', 'KESC - Kendall Endoscopy Surgery Center', 'KIEC - Kissimmee Endoscopy Center', 'KSC - Kissimmee Surgical Center', 'LSC - Laser and Surgery Center', 'OSS - Outpatient Surgical Services', 'PALMS W SC - Palms W Surgicenter', 'PSC - Parkcreek Surgery Center', 'SLSC - Sand Lake Surgery Center', 'SFSC - South Florida Surgical Center', 'SPSC - Summerport Surgery Center', 'SCCS - Surgery Center at Coral Springs', 'SCOA - Surgery Center Of Aventura', 'TOCBOY - The Outpatient Center of Boynton Beach', 'USC - University Surgery Center', 'VASC - Venture Ambulatory Surgical Center', 'WOSC - Weston Outpatient Surgical Center', 'SCFL - Surgery Center at Ft. Lauderdale']
import time
import pyautogui
from pynput.keyboard import Key, Controller
import time
import keyboard

for i in range(len(l)):
    import keyboard
    time.sleep(3)
    locate = pyautogui.locateOnScreen('Screenshot 2024-10-28 173223.png',confidence=0.8)
    center = pyautogui.center(locate)
    pyautogui.doubleClick(center)
    time.sleep(3)
    keyboard.write(l[i])
    time.sleep(2)
    keyboard.press_and_release('down')
    keyboard.press_and_release('enter')

        #click in total
    time.sleep(7)
    locate = pyautogui.locateOnScreen("C:\\Users\\Yashwanth.Akuthota\\Pictures\\Screenshots\\Screenshot 2024-10-29 083927.png",confidence=0.8)
    center = pyautogui.center(locate)
    pyautogui.doubleClick(center)
        #total->268,401

        #press the download button
        
    time.sleep(4)
    locate = pyautogui.locateOnScreen('images-gastro\Screenshot 2024-10-28 145712.png',confidence=0.8)
    center = pyautogui.center(locate)
    pyautogui.doubleClick(center)

        #click on the black download icon next
        
    time.sleep(4)
    locate = pyautogui.locateOnScreen('images-gastro\Screenshot 2024-10-28 145755.png',confidence=0.8)
    center = pyautogui.center(locate)
    pyautogui.doubleClick(center)

    time.sleep(6)
    #for hotkey to go back
    #kb = Controller()
    #kb.press(Key.alt)
    #kb.press(Key.left)
    #kb.release(Key.alt)
    #kb.release(Key.left)
    keyboard.press_and_release("alt+left")

    time.sleep(2)
    
    #reload,just call the image
    locate = pyautogui.locateOnScreen('C:\\Users\\Yashwanth.Akuthota\\Desktop\\jquery\\Screenshot 2024-10-29 115752.png',confidence=0.8)
    center = pyautogui.center(locate)
    pyautogui.doubleClick(center)

    #kb.press(Key.ctrl)
    #keyboard.press('r')
    #keyboard.press('r')
    #kb.release(Key.ctrl)
