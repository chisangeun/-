from bs4 import BeautifulSoup
from selenium import webdriver
import requests


def get_daum_news_title(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, "html.parser")
    title_tag = soup.select_one('h3.tit_view')
    if title_tag:
        print(title_tag.get_text())
    else:
        print("안됨")


if __name__ == '__main__':
    get_daum_news_title(20190728165812603)
    get_daum_news_title('20190801114158041')
