from selenium import webdriver

import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def graph():

    url = 'https://opensea.io/collection/okay-bears?tab=activity'
    driver = webdriver.Chrome('/Users/sangeun/Downloads/chromedriver')

    driver.implicitly_wait(1)

    driver.get(url)

    content=driver.find_element(By.CSS_SELECTOR,'g.recharts-layer recharts-bar-rectangle')
    height=content.get_attribute('height')
    print(height)

graph()