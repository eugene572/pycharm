import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEx1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_ex1(self):
        self.driver.get("https://portal.daou.co.kr/login")
        self.driver.set_window_size(1011, 840)
        self.driver.find_element(By.ID, "username").send_keys("yoojin1216")
        self.driver.find_element(By.ID, "password").send_keys("suji10815!")
        self.driver.find_element(By.CSS_SELECTOR, ".login_box:nth-child(1)").click()

        # 로그인 후 페이지가 완전히 로드될 때까지 기다립니다.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "login_submit")))

        self.driver.find_element(By.ID, "login_submit").click()

        # 페이지가 완전히 로드될 때까지 대기합니다.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

        self.driver.close()
