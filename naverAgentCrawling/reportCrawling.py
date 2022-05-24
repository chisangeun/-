import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 동향보고서 => 수치를 그래프로 표현 가능
def get_report(lng):
    driver=webdriver.Chrome('/Users/sangeun/Downloads/chromedriver')
    url='https://land.naver.com/news/trendReport.naver'

    driver.implicitly_wait(1)

    driver.get(url)
    time.sleep(2)

    container=driver.find_element(By.CSS_SELECTOR,'tbody')
    tr=container.find_elements(By.CSS_SELECTOR,'tr')

    chk=0 # 관리자가 원하는 기간 사이의 정보만 크롤링 하기 위한 변수
    for i in tr:
        text=i.find_element(By.CSS_SELECTOR,'td.txt > a')
        href=i.find_element(By.CSS_SELECTOR,'td.txt > a').get_attribute('href')
        if chk>=lng:
            break
        print(text.text)
        print("링크",href)
        chk+=1
    # 만약 페이지가 넘어가면 ?


if __name__=='__main__':
    lng=int(input("최근 몇 주간 동향보고서를 크롤링할것인가? "))
    get_report(lng)
