from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#웹드라이브의 경로를 입력한다.
path = "C:\\Users\\kbs\\Documents\\programing\\puyopuyo\\coding_quizzes\\chromedriver.exe"

driver = webdriver.Chrome(path)
# driver.get('https://google.com')
# search_box = driver.find_element_by_name('q')
# search_box.send_keys("도화재 석문호흡")
# search_box.submit()


#니코동에 로그인을 해보자.

login_url_id = "siteHeaderNotification"
email_id = "input__mailtel"
email_value = "kmmokmmo@naver.com"
password_id = "input__password"
password_value = "********"


driver.get('https://www.nicovideo.jp/')
login = driver.find_element_by_id(login_url_id)
login.click()

email_input = driver.find_element_by_id(email_id)
email_input.send_keys(email_value)

password_input = driver.find_element_by_id(password_id)
password_input.send_keys(password_value)

password_input.send_keys(Keys.RETURN)
