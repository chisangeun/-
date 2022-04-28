from selenium import webdriver

import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def search():
    url='https://opensea.io/'
    driver = webdriver.Chrome('/Users/sangeun/Downloads/chromedriver')

    driver.implicitly_wait(1)

    driver.get(url)

    driver.find_element(By.CSS_SELECTOR,'div.Inputreact__StyledContainer-sc-3dr67n-0').click()
    element=driver.find_element(By.CSS_SELECTOR,'input')
    element.send_keys("Okay Bears")
    element.send_keys(Keys.RETURN)

    time.sleep(2)
    driver.quit()


search()