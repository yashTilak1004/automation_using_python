'''f
rom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

#all purpose selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.get('https://ui.vision/demo/webtest/frames/')

driver.find_element('name','mytext1').send_keys("First info.")
time.sleep(10)
#driver.find_element_by_name('first_name').send_keys("my_first_name")
'''
'''
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://ui.vision/demo/webtest/frames/"
driver.get(url)
'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Open the URL with frames
url = "https://ui.vision/demo/webtest/frames/"
driver.get(url)
# Switch to Frame 1

def frame_1(frame_src, input_name, input_value):
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH, '//*[@id="id1"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)
        print(f"Filled {input_name} with value: {input_value}")
    except Exception as e:
        print(f"Error filling input {input_name}: {e}")
    finally:
        driver.switch_to.default_content()

def frame_2(frame_src, input_name, input_value):
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH, '//*[@id="id2"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)
        print(f"Filled {input_name} with value: {input_value}")
    except Exception as e:
        print(f"Error filling input {input_name}: {e}")
    finally:
        driver.switch_to.default_content()

def frame_4(frame_src, input_name, input_value):
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH, '//*[@id="id4"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)
        print(f"Filled {input_name} with value: {input_value}")
    except Exception as e:
        print(f"Error filling input {input_name}: {e}")
    finally:
        driver.switch_to.default_content()

def frame_5(frame_src, input_name, input_value):
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH, '//*[@id="id5"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)
        driver.find_element_by_link_text('/html/body/center/a').click()
        print(f"Filled {input_name} with value: {input_value}")
    except Exception as e:
        print(f"Error filling input {input_name}: {e}")
    finally:
        driver.switch_to.default_content()







frame_1("frame_1.html","mytext1","abcdwe")
time.sleep(1)

frame_1("frame_2.html","mytext2","abcdwe")
time.sleep(1)

frame_1("frame_4.html","mytext4","abcdwe")
time.sleep(1)

frame_1("frame_5.html","mytext5","abcdwe")
time.sleep(1)

'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the URL with frames
url = "https://ui.vision/demo/webtest/frames/"
driver.get(url)

def fill_input_in_frame(frame_src, input_id, input_value):
    # Switch to the specified frame
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH, f'//*[@id="{input_id}"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)

        if(input_id == "id3"):
            
            driver.find_element(By.CLASS_NAME,'Od2TWd hYsg7c').click()
            time.sleep(3)
            


        if(input_id == 'id5'):
            driver.find_element(By.XPATH,"/html/body/center/a").click()
            time.sleep(3)
        print(f"Filled {input_id} with value: {input_value}")
        
    except Exception as e:
        print(f"Error filling input {input_id}: {e}")
    finally:
        # Switch back to the default content after operation
        driver.switch_to.default_content()

# Fill inputs in the respective frames
frame_inputs = [
    ("frame_1.html", "id1", "abcdwe"),
    ("frame_2.html", "id2", "abcdwe"),
    {"frame_3.html","id3","abcdwe"},
    ("frame_4.html", "id4", "abcdwe"),
    ("frame_5.html", "id5", "abcdwe"),
]

for frame_src, input_id, input_value in frame_inputs:
    fill_input_in_frame(frame_src, input_id, input_value)
    time.sleep(1)

# Close the driver
driver.quit()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the URL with frames
url = "https://ui.vision/demo/webtest/frames/"
driver.get(url)

def fill_input_in_frame(frame_src, input_id, input_value):
    # Switch to the specified frame
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH, f'//*[@id="{input_id}"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)
        print(f"Filled {input_id} with value: {input_value}")

        #/html/body/center/iframe
        if input_id == "id3":
            r = driver.find_element(By.XPATH,'/html/body/center/iframe')
            driver.switch_to.frame(r)
            driver.maximize_window()
            driver.find_element(By.XPATH, '//*[@id="i5"]').click()
            time.sleep(2)
            driver.find_element(By.XPATH,'//*[@id="i19"]').click()
            time.sleep(2)
            driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div').click()
            time.sleep(2)
            driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[4]').click()
            time.sleep(2)
            driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div[1]/div[1]/div/span').click()
            time.sleep(2)
            ip = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            ip.clear()
            ip.send_keys("Text 1")
            time.sleep(2)
            ip = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
            ip.clear()
            ip.send_keys("Text 2")
            time.sleep(2)
            #submit button
            driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/span/span').click()
            time.sleep(1)
        if input_id == 'id5':
            #driver.maximize_window()
            driver.find_element(By.XPATH, "/html/body/center/a").click()
            time.sleep(3)

        
        
    except Exception as e:
        print(f"Error filling input {input_id}: {e}")
    finally:
        # Switch back to the default content after operation
        driver.switch_to.default_content()

# Fill inputs in the respective frames
frame_inputs = [
    ("frame_1.html", "id1", "abcdwe"),
    ("frame_2.html", "id2", "abcdwe"),
    ("frame_3.html", "id3", "abcdwe"), 
    ("frame_4.html", "id4", "abcdwe"),
    ("frame_5.html", "id5", "abcdwe"),
]

for frame_src, input_id, input_value in frame_inputs:
    fill_input_in_frame(frame_src, input_id, input_value)
    time.sleep(1)

driver.quit()  # Close the driver after finishing
