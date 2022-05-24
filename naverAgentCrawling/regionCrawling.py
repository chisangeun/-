import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def get_region_info():
    url = 'https://land.naver.com/news/region.naver'
    driver = webdriver.Chrome('/Users/sangeun/Downloads/chromedriver')

    # 일시적 대기
    driver.implicitly_wait(1)

    # 페이지 이동
    driver.get(url)
    time.sleep(2)

    # 드롭다운형식 옵션 선택하기
    region = Select(driver.find_element(By.ID,'city_no'))
    region.select_by_visible_text('서울')

    city=Select(driver.find_element(By.ID,'dvsn_no'))
    city.select_by_visible_text('서초구')


    # 뉴스 헤드라인 & 링크 & 날짜 크롤링 ** elements => 배열로 저장!!!!
    container=driver.find_element(By.CSS_SELECTOR,'ul.headline_list')
    li = container.find_elements(By.CSS_SELECTOR,'li')

    for i in li:
        header=i.find_element(By.CSS_SELECTOR,'dt > a > img').get_attribute('alt')
        href=i.find_element(By.CSS_SELECTOR,'dt > a').get_attribute('href')
        day=i.find_element(By.CSS_SELECTOR,'dd > span.date').text
        print("기사 제목: ",header)
        print("기사링크: ",href)
        print("작성일 :", day)

    time.sleep(3)


if __name__ == '__main__':
    get_region_info()
