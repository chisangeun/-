from bs4 import BeautifulSoup
import requests

def get_daum_news_text(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp=requests.get(url)

    soup=BeautifulSoup(resp.text,"html.parser")
    content=''
    for i in soup.select('div#harmonyContainer p'):
        content+=i.get_text()
    return content

if __name__=='__main__':
   print(get_daum_news_text('20190728165812603'))
   print('\n')
   print(get_daum_news_text('20190801114158041'))
