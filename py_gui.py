'''
a,href,rel=bookmark
'''
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
#scrape a webpage
driver = webdriver.Chrome('/Users/MyUsername/Downloads/chromedriver')
driver.get('https://www.factcheck.org/')
data= driver.find_elements_by_xpath('//a[@rel="bookmark"]')
titles = []
for i in range(len(data)):
    titles.append(data)
'''

#selenium
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Set up Chrome options
chrome_options = Options()

# Set the path for the ChromeDriver
service = Service('C:\\Users\\Yashwanth.Akuthota\\Desktop\\jquery\\chromedriver.exe')

# Set up the Chrome driver with the specified options and service
driver = webdriver.Chrome(service=service, options=chrome_options)

# Rest of your code
driver.get('https://www.factcheck.org/')
data = driver.find_elements(By.XPATH, '//a[@rel="bookmark"]')
titles = []

for element in data:
    titles.append(element.text)

df = pd.DataFrame(titles, columns=['Titles'])
df.to_csv('factcheck_titles.csv', index=False)

driver.quit()
'''


#.moveTo(X-coordinates,Y-coordinates)=>move the mouse coordinates->(100,100)
#.click()=>left mouse movement
#.typewrite("text")=>types the text
#.hotkey("a,b")=>simulates hotkey(2 key's pressed at once)
'''
import pyautogui
import time
from pyscreeze import ImageNotFoundException

pyautogui.press('win')#press('some application')=>win means press windows key
pyautogui.typewrite('Chrome')#type chrome in "search for apps,documents"
pyautogui.press('enter')#open chrome
time.sleep(2)
pyautogui.typewrite('wikipedia.org')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl','a')
pyautogui.screenshot('ss1.png')
'''
'''
import pyautogui
# force use of ImageNotFoundException
pyautogui.useImageNotFoundException()

try:
    location = pyautogui.locateOnScreen('C:\\Users\\Yashwanth.Akuthota\\Desktop\\jquery\\ss.png')
    print('image found')
except pyautogui.ImageNotFoundException:
    print('ImageNotFoundException: image not found')
'''
'''
pyautogui.hotkey('win','r')
pyautogui.typewrite("notepad.exe")
pyautogui.press('enter')
'''
'''
time.sleep(3)
pyautogui.hotkey('alt','tab')
time.sleep(2)
pyautogui.hotkey('alt','shift','tab')
pyautogui.hotkey('win','down')
'''
# Type data into a form
'''
data = ['Henil Shah', 'henilshah@email.com', '12345-67890']
time.sleep(4)
for item in data:
    pyautogui.typewrite(item + '\t')
'''
#pyautogui can be combined with selenium for scraping
'''
from selenium import webdriver
import pyautogui
# Open a webpage with Selenium
driver = webdriver.Chrome()
driver.get('https://google.com')
# Use PyAutoGUI to perform tasks on the page
pyautogui.typewrite('Hello, PyAutoGUI!')
'''

'''
import pyautogui
import time
pyautogui.hotkey('win','r')
pyautogui.typewrite("MSTSC")
time.sleep(2)
pyautogui.press('enter')
#get to rdp
time.sleep(2)
pyautogui.press('enter')
#get to password position
time.sleep(2)
pyautogui.typewrite('Marshall$25')
#time.sleep(2)
#now go to the rdp
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('left')
pyautogui.press('enter')
time.sleep(4)
pyautogui.hotkey('win','r')
#calc
time.sleep(1)
pyautogui.typewrite('calc')
pyautogui.press('enter')
time.sleep(1)
#type on calculator
pyautogui.typewrite('33')
pyautogui.hotkey('shift','=')
pyautogui.typewrite('44')
pyautogui.press('=')
'''

'''
import pyautogui
import time

time.sleep(1)
pyautogui.hotkey('ctrl','shift','`')
time.sleep(1)
pyautogui.typewrite('python Read_pdf_img.py')
pyautogui.press('enter')
'''

'''
import pyautogui
import time
import subprocess
def open_remote_desktop():
    subprocess.Popen(['mstsc'])
    time.sleep(2)
def enter_credentials(username, password):
    pyautogui.typewrite(username)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite(password)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
def open_chrome():
    pyautogui.press('win')
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite('http://appstaging.datamarshall.com/q-revoptima/')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
def place_coordinates():
    pyautogui.moveTo(1047,587)
    time.sleep(2)
    pyautogui.typewrite("vishaltest@dm.com")
    time.sleep(2)
    pyautogui.moveTo(1056,587)
    time.sleep(2)
    pyautogui.click(button=1)
    time.sleep(1)
    pyautogui.moveTo(1042,642)
    time.sleep(2)
    pyautogui.typewrite("Pass@1234")
    time.sleep(2)
    pyautogui.press('enter')
if __name__ == "__main__":
    open_remote_desktop()
    enter_credentials('172.21.72.116', 'Marshall$25')
    open_chrome()
    place_coordinates()
'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

#all purpose selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.get('https://www.google.com/')
'''

'''
import requests
response = requests.get("http://api.open-notify.org/astros")
import json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json()) Fourth Frame    Fifth Frame
'''
import time
import pyautogui
#open edge
pyautogui.press('win')
pyautogui.typewrite('c')
pyautogui.press('enter')
time.sleep(1)
#in edge
pyautogui.typewrite('https://ui.vision/demo/webtest/frames/')
pyautogui.press('enter')
time.sleep(1)
#type in each frame
pyautogui.press('tab')
pyautogui.typewrite('First Frame')
time.sleep(1)
pyautogui.press('tab')
pyautogui.typewrite('Second Frame')
time.sleep(1)
pyautogui.press('tab')
#to third and fourth frame
pyautogui.typewrite('Third Frame')
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('down')
#next form
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('space')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(1)
#first half form done
pyautogui.press('tab')
pyautogui.press('enter')
#pyautogui.moveTo(535,557)
#pyautogui.click()

time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite('short text')
pyautogui.press('tab')
pyautogui.typewrite('long text')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)
#fourth
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite('Fourth Frame')

pyautogui.press('tab')
pyautogui.typewrite('Fifth Frame')

pyautogui.press('tab')
pyautogui.press('enter')