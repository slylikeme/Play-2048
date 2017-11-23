#! python3
# play2048.py - plays online 2048 browser game like a toddler might

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import gc

gc.enable()

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

elem = browser.find_element_by_css_selector('html')
retry = browser.find_element_by_css_selector('.retry-button')

# while loop that "plays" 2048 by rolling its forehead on the arrow keys
while True:
    elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.LEFT)
    elem.send_keys(Keys.RIGHT)
    elem.send_keys(Keys.LEFT)
    elem.send_keys(Keys.RIGHT)
    elem.send_keys(Keys.UP)
    elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.LEFT)
    elem.send_keys(Keys.RIGHT)
    elem.send_keys(Keys.LEFT)
    elem.send_keys(Keys.RIGHT)
    try:
        retry.click()
        time.sleep(1)
    except:
        continue



# this is the try again html selector -> '.retry-button'
