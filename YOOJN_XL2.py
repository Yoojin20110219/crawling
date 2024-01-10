from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv) #기본 창 윈도우설정

import time, datetime, os
import openpyxl   #모듈 호출

now = str(datetime.datetime.now())[:16]
folderName = now.replace(":", "_")
os.mkdir(folderName) #파일 이름 날짜로 저장

key_word = ["공모주"]#검색어 입력

wb= openpyxl.Workbook()#액셀파일 만들기

for i in range(len(key_word)):
    ws = wb.create_sheet()   #워크시트 만들기
    ws.title = key_word[i]

    url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + key_word[i]
    driver.get(url)
    time.sleep(2)
