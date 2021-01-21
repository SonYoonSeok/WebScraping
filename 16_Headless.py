from selenium import webdriver
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")



browser = webdriver.Chrome(options = options)
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

import time
interval = 2 # 2 초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    #페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

print("스크롤 완료")

# bs4

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class" : ["Vpfmgd"]})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    # 할인 전 가격 정보
    # original_price = movie.find("span", attrs={"span" : "SUZt4c djCuy"})
    # if original_price:
    #     original_price = original_price.get_text()
    # else:
    #     continue
       # print(title, " <할인되지 않은 영화 제외>")

    # 할인 된 가격
    price = movie.find("span", attrs={"span":"VfPpfd ZdBevf i5DZme"}).get_text()

    link = movie.find("a", attrs={"class" : "JC71ub"})["href"]
    
    print(f"제목 : {title}")
    #print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)

browser.quit()

