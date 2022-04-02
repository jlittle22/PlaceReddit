import os
from dotenv import load_dotenv

load_dotenv()

uname = os.getenv('USERNAME')
pword = os.getenv('PASSWORD')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Firefox()
driver.maximize_window() # For maximizing window
driver.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")

elem = driver.find_element(By.ID, "loginUsername")
elem.send_keys(uname)
elem = driver.find_element(By.ID, "loginPassword")
elem.send_keys(pword)
elem = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button")
elem.click()

time.sleep(10)
# https://www.reddit.com/r/place/?cx=277&cy=32&px=52
x = 100
y = 1000
driver.get(f"https://www.reddit.com/r/place?cx={x}&cy={y}&px=52")

time.sleep(5)
elem = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div")
elem.click()
time.sleep(5)


# GET HTE FUCK BUTTON!!!
try:
    elem = driver.find_element(By.XPATH, "/div/mona-lisa-share-container/div[4]/mona-lisa-status-pill")
    elem.click()
except:
    time.sleep(5)
    elem = driver.find_element(By.CLASS_NAME, "bottom-controls")
    elem.click()

time.sleep(5)

# elem = driver.find_element(By.XPATH, "/div/canvas")
# action = webdriver.common.action_chains.ActionChains(driver)
# x_coord = int(driver.find_element_by_xpath(elem).location['x'])
# y_coord = int(driver.find_element_by_xpath(elem).location['y'])
# width = int(driver.find_element_by_xpath(elem).size['width'])
# height = int(driver.find_element_by_xpath(elem).size['height'])
# action.move_by_offset(x_coord + width/2, y_coord + height/2)
# action.click()
# action.perform()




while 1:
    pass

assert "No results found." not in driver.page_source
driver.close()