from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

url = "https://search.naver.com/search.naver?&where=news&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
articles=soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
#sp_nws1 > div.news_wrap.api_ani_send > a
for article in articles:
    title = article.select_one('div.news_wrap.api_ani_send > div > a').text
    url = article.select_one('div.news_wrap.api_ani_send > div > a')['href']
    comp = article.select_one('a.info.press').text.split(' ')[0].replace('언론사','')
    thumnails = article.select_one('div.news_wrap.api_ani_send > a')['href']
    ws1.append([title,url,comp,thumnails])

wb.save(filename='articles.xlsx')
driver.quit()