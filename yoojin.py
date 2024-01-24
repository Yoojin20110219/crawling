'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
driver.get("https://www.naver.com")

driver=webdriver.Chrome()
driver.get("https://www.naver.com")

driver.maximize_window()'''#창 최대화
'''driver.minimize_window()'''#창 최소화
'''driver.set_window_size(700,700)'''#창 사이즈 조절
'''driver.set_window_position(0,0)'''#창위치 조정


'''u=["http://naver.com","http://youtube.com","http://google.com"]
d=[]

import time
for i in range(len(u)):
    driver=webdriver.Chrome()
    d.append(driver)
    time.sleep(1)

for i in range(len(u)):
    d[i].get(u[i])

input("엔터치면 창이 닫칩니다")

for i in range(len(u)):
   d[i].close()
'''
#테스트사이트 웹크롤링
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

driver.get("https://sbasu.pythonanywhere.com/tastyFoodApp/")
p='//*[@id="homePageLinks"]/ul/li/a'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_firstName"]'
e=driver.find_element('xpath',p)
e.send_keys('yoojin')
           
p='//*[@id="id_lastName"]'
e=driver.find_element('xpath',p)
e.send_keys('lim')

p='//*[@id="id_gender_1"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_username"]'
e=driver.find_element('xpath',p)
e.send_keys('Dive forever')

p='//*[@id="id_password"]'
e=driver.find_element('xpath',p)
e.send_keys('GYRWLL')

p='//*[@id="id_state"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_state"]/option[2]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_fee"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_fee"]/option[3]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_date"]'
e=driver.find_element('xpath',p)
e.send_keys('11/8/9999')

p='/html/body/form/div/input'
e=driver.find_element('xpath',p)
e.click()
'''
#위드뮤
'''import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
driver.maximize_window()

driver.get("https://www.withmuu.com/")

time.sleep(2)
p='//*[@id="header"]/div/div[3]/ul/li[2]/button/i'
e=driver.find_element('xpath',p)
e.click()

time.sleep(2)
p='//*[@id="search_form"]'
e=driver.find_element('xpath',p)
e.send_keys('아이브')

time.sleep(2)
p='//*[@id="btnSearchTop"]'
e=driver.find_element('xpath',p)
e.click()


#엔터치기
'''from selenium.webdriver.common.keys import  Keys
e.send_keys(Keys.RETURN)
'''
#..초기다리기
'''import time
time.sleep()
'''

#유튜브 검색
'''import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)'''
#필요x(위 코드안에 포함)
'''driver.get("https://www.youtube.com/results?search_query=baddie")

p='//input[@id="search"]'
e=driver.find_element('xpath',p)
e.click()
e.send_keys('baddie')
from selenium.webdriver.common.keys import  Keys
e.send_keys(Keys.RETURN)
time.sleep(2)

p1='//a[@id="thumbnail"]'
elements=driver.find_elements('xpath',p1)

time.sleep(2)

driver.get(elements[1].get_attribute("href"))
'''

#학교종이
'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
import time
driver.get("https://schoolbell-e.com/ko/main/home")
time.sleep(3)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-home/div[1]/div[3]/div[1]/div/button[1]'
e=driver.find_element('xpath',p)
e.click()  # 이 코드가 빠져있어서 실행이 안됐던 거야~
time.sleep(3)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[1]/div/phone-number-input/div/input'
e=driver.find_element('xpath',p)
e.send_keys('01045498182')

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[2]/div[1]/input'
e=driver.find_element('xpath',p)
e.send_keys('quf35078152')


p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[3]/button'
e=driver.find_element('xpath',p)
e.click()
time.sleep(3)

p='/html/body/app-root/app-main/div[1]/app-main-home/div[2]/div[1]/div[1]/app-my-group-slides/div/ngu-carousel/div/div[1]/div/ngu-tile[1]/div/div[1]/div/div[1]'
e=driver.find_element('xpath',p)
e.click()
time.sleep(2)
'''

#안내문 출력(fomat 활용하기)
'''file=open('학교종이.txt','w')
for i in range(10):
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/h6/app-translation-viewer/span'
    e=driver.find_element('xpath',p)
    file.write(e.text+'\n')
file.close()



textttttt="가나다라마바사아자차카타파하"
file.write(textttttt)
file.close()
'''
#네이버 뉴스 검색창 캡쳐
'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)


ive=['아이브 리즈','아이브 가을','아이브 원영','아이브 유진','아이브 레이','아이브 이서']
driver.maximize_window()
for i in range(len(ive)):
    driver.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query="+ ive[i])
    driver.save_screenshot( ive[i]+".png")'''





























