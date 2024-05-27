from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_te1 import __doClick_log


def doFindByLinkText_Click(driver, linkText, printStr):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, linkText)))
    driver.find_element(By.LINK_TEXT, linkText).click()
    __doClick_log(printStr)

# 웹 드라이버 초기화
driver = webdriver.Chrome()

# 대우 오피스 로그인 페이지로 이동
driver.get("https://nstaging.daouoffice.com/login")
driver.set_window_size(1187, 812)

# 로그인 입력 필드에 유저네임 입력
driver.find_element(By.ID, "username").send_keys("yoojin1216")

# 로그인 입력 필드에 패스워드 입력 후 엔터
driver.find_element(By.ID, "password").send_keys("1qaz2wsx#")
driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

try:
    # 페이지 로딩을 기다립니다.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "홈")))
    # "홈" 링크를 클릭합니다.
    doFindByLinkText_Click(driver, "홈", "로그인에 성공하였습니다")
    print("로그인에 성공하였습니다")
except Exception as e:
    # 예외가 발생했을 때 처리할 코드
    print("로그인에 실패했습니다:", e)
