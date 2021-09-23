import dload
from bs4 import BeautifulSoup   #beautifulsoup 이용하겠다.
from selenium import webdriver  #seleniu 이용하겠다.
import time

driver = webdriver.Chrome('chromedriver')   # 웹드라이버 파일의 경로 드라이버 다운해주세요
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EA%B9%80%EA%B3%A0%EC%9D%80")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source            #페이지 에서 받아온 결과 모두 저장

soup = BeautifulSoup(req, 'html.parser')

# print(soup)         #원하는 부분 출력
thumbnails = soup.select('#imgList > div > a > img')
i=1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img,f'imgs_homework/{i}.jpg')
    i += 1
driver.quit() # 끝나면 닫아주기
