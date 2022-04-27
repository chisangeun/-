import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def find_building():
    url='https://realty.daum.net/'
    driver=webdriver.Chrome('/Users/sangeun/Downloads/chromedriver')

    driver.implicitly_wait(1)

    driver.get(url)

    container=driver.find_element(By.CSS_SELECTOR,'div.sc-fnlXEO')
    select=container.find_elements(By.CSS_SELECTOR,'div.sc-dYzmtA')
    print(select[0].text)


if __name__=='__main__':
    # a=input("어떤 유형 (아파트, 빌라/투룸 , 원룸, 오피스텔) 의 매물을 찾고있나요?")
    # if a=='아파트':
    #     b=input("매물 or 분양 중 어떤 유형의 매물을 찾고있나요?")
    find_building()
