import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def final_crawling():
    driver = webdriver.Chrome('/Users/sangeun/Downloads/chromedriver')
    url = 'https://land.naver.com/news/trendReport.naver'

    driver.implicitly_wait(1)

    driver.get(url)
    time.sleep(2)

if __name__ == '__main__':
    final_crawling()