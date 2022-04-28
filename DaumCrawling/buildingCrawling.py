import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def find_building(type, option):
    url = 'https://realty.daum.net/'
    driver = webdriver.Chrome('/Users/sangeun/Downloads/chromedriver')

    driver.implicitly_wait(1)

    driver.get(url)

    container = driver.find_element(By.CSS_SELECTOR, 'div.sc-fnlXEO')
    # select=container.find_elements(By.CSS_SELECTOR,'div.sc-dYzmtA')
    click = container.find_elements(By.CSS_SELECTOR, 'div.sc-gfHBtU')

    # 타입 별로 매물 검색
    if type == '아파트':
        if option == '매물':
            click[0].click()
            time.sleep(2)
            # old_apt()
        elif option == '분양':
            click[1].click()
            time.sleep(2)
            # 이런식으로 해당 페이지에서 데이터 크롤링 가능
            select=driver.find_element(By.CSS_SELECTOR,'div.Wrap__PageWrapper-oyn6j3-0')
            print(select.text)
    elif type == '빌라/투룸':
        click[2].click()
        time.sleep(2)
        # villa()
    elif type == '원룸':
        click[3].click()
        time.sleep(2)
        # oneRoom()
    elif type == '오피스텔':
        click[4].click()
        time.sleep(2)
        # off()

    time.sleep(5)

if __name__ == '__main__':
    b = ''
    a = input("어떤 유형 (아파트, 빌라/투룸 , 원룸, 오피스텔) 의 매물을 찾고있나요?")
    if a == '아파트':
        b = input("매물 or 분양 중 어떤 유형의 매물을 찾고있나요?")
    find_building(a, b)
