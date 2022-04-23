
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



def get_agent_info():
    url = 'https://land.naver.com/news/region.naver'
    driver = webdriver.Chrome('/Users/sangeun/Downloads/chromedriver')

    # 일시적 대기
    driver.implicitly_wait(1)

    # 페이지 이동
    driver.get(url)
    time.sleep(2)

    select=Select(driver.find_element(By.CSS_SELECTOR,'option'))
    select.select_by_value(value='전남')


    # 로딩 완료 후 유지시간
    # time.sleep(3)



if __name__ == '__main__':
    get_agent_info()
