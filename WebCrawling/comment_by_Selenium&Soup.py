from bs4 import BeautifulSoup
import requests


def get_daum_news_comment():
    url = 'https://stat.tiara.daum.net/track?d=%7B%22sdk%22%3A%7B%22type%22%3A%22WEB%22%2C%22version%22%3A%221.1.20' \
          '%22%7D%2C%22env%22%3A%7B%22screen%22%3A%221440X900%22%2C%22tz%22%3A%22%2B9%22%2C%22cke%22%3A%22Y%22%7D%2C' \
          '%22common%22%3A%7B%22session_timeout%22%3A%221800%22%2C%22svcdomain%22%3A%22media.daum.net%22%2C' \
          '%22deployment%22%3A%22production%22%2C%22url%22%3A%22https%3A%2F%2Fnews.v.daum.net%2Fv%2F20190728165812603' \
          '%22%2C%22title%22%3A%22%EC%9D%BC%EB%A1%A0%EB%A8%B8%EC%8A%A4%ED%81%AC%20%5C%22%ED%85%8C%EC%8A%AC%EB%9D%BC' \
          '%EC%97%90%EC%84%9C%20%EB%84%B7%ED%94%8C%EB%A6%AD%EC%8A%A4%C2%B7%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EC%A6%90%EA' \
          '%B8%B8%20%EB%82%A0%20%EC%98%A8%EB%8B%A4%5C%22%22%2C%22section%22%3A%22digital%22%2C%22page%22%3A' \
          '%22newsview%22%7D%2C%22page_meta%22%3A%7B%22id%22%3A%2220190728165812603%22%2C%22type%22%3A%22article%22' \
          '%2C%22name%22%3A%22%EC%9D%BC%EB%A1%A0%EB%A8%B8%EC%8A%A4%ED%81%AC%20%5C%22%ED%85%8C%EC%8A%AC%EB%9D%BC%EC%97' \
          '%90%EC%84%9C%20%EB%84%B7%ED%94%8C%EB%A6%AD%EC%8A%A4%C2%B7%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EC%A6%90%EA%B8%B8' \
          '%20%EB%82%A0%20%EC%98%A8%EB%8B%A4%5C%22%22%2C%22category_id%22%3A%22100031%22%2C%22category%22%3A' \
          '%22digital%22%2C%22author%22%3A%22%EC%9D%B4%EB%AF%BC%EC%9A%B0%22%2C%22author_id%22%3A%22letzwin%40asiae.co' \
          '.kr%22%2C%22provider%22%3A%22%EC%95%84%EC%8B%9C%EC%95%84%EA%B2%BD%EC%A0%9C%22%2C%22provider_id%22%3A%2290' \
          '%22%2C%22regdate%22%3A%222019-07-28%2016%3A58%3A12%22%2C%22plink%22%3A%22https%3A%2F%2Fmedia.daum.net%2Fv' \
          '%2F20190728165812603%22%2C%22image%22%3A%22https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F201907%2F28%2Fakn' \
          '%2F20190728165813230vjsq.jpg%22%2C%22harmony_consumer_id%22%3A%22media%22%2C%22media%22%3A%22pcweb%22%7D' \
          '%2C%22etc%22%3A%7B%22client_info%22%3A%7B%22tuid%22%3A%22w-pArxFZhPKjRm_220419205817114%22%2C%22tsid%22%3A' \
          '%22w-pArxFZhPKjRm_220419205817114%22%2C%22uuid%22%3A%22w-4eBE28ovAHrd_220419322220199%22%2C%22suid%22%3A' \
          '%22w-4eBE28ovAHrd_220419322220199%22%7D%7D%2C%22action%22%3A%7B%22type%22%3A%22Event%22%2C%22name%22%3A%22' \
          '%EB%8C%93%EA%B8%80%EB%AA%A9%EB%A1%9D_%EB%8D%94%EB%B3%B4%EA%B8%B0%22%2C%22kind%22%3A%22%22%7D%2C%22click%22' \
          '%3A%7B%22layer1%22%3A%22pc_news%22%2C%22layer2%22%3A%22pc_comment%22%2C%22layer3%22%3A%22%22%2C' \
          '%22click_url%22%3A%22%22%2C%22ordnum%22%3A29%2C%22copy%22%3A%22%EB%8D%94%EB%B3%B4%EA%B8%B0%22%2C%22image' \
          '%22%3A%22%22%2C%22posX%22%3A428%2C%22posY%22%3A382%7D%2C%22custom_props%22%3A%7B%22contentUniqueKey%22%3A' \
          '%22hamny-20190728165812603%22%2C%22docId%22%3A%22NHT9NtZWBe%22%2C%22harmony_consumer_id%22%3A%22media%22' \
          '%2C%22media%22%3A%22pcweb%22%2C%22reg_dt%22%3A%222019-07-28%2016%3A58%3A12%22%2C%22reg_timestamp%22%3A' \
          '%221564300692871%22%2C%22alex.view%22%3A%22main%22%2C%22alex.component%22%3A%22single%22%2C%22alex' \
          '.clientId%22%3A%2226BXAvKny5WF5Z09lr5k77Y8%22%2C%22alex.forumId%22%3A%22-99%22%2C%22alex.postKey%22%3A' \
          '%2220190728165812603%22%7D%7D '
    resp = requests.get(url)
    resp.json()
    # soup=BeautifulSoup(resp.text)


if __name__ == '__main__':
    get_daum_news_comment()
