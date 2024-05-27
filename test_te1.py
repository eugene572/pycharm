from distutils.command.config import config
from lib2to3.pgen2 import driver

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTe1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def doFindByLinkText_Click(linkText, printStr):
        WebDriverWait(driver, float(config['system']['WAIT_TERM'])).until(EC.presence_of_element_located((By.LINK_TEXT, linkText)))
        driver.find_element(By.LINK_TEXT, linkText).click()
        # __doClick_log(printStr)  # __doClick_log 함수 정의가 필요합니다.

    def test_te1(self):
        self.driver.get("https://nstaging.daouoffice.com/login")
        self.driver.set_window_size(1187, 812)

        # 로그인 입력 필드에 유저네임 입력
        self.driver.find_element(By.ID, "username").send_keys("yoojin1216")

        # 로그인 입력 필드에 패스워드 입력 후 엔터
        self.driver.find_element(By.ID, "password").send_keys("1qaz2wsx#")
        self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

        try:
            # 페이지 로딩을 기다립니다.
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "홈")))
            # # "홈" 링크를 클릭합니다.
            # self.driver.find_element(By.LINK_TEXT, "홈").click()
            # time.sleep(3)
            print("로그인에 성공하였습니다")

        except Exception as e:
            #예외가 발생했을 때 처리할 코드
            print("로그인에 실패했습니다:", e)

        try:
            # 페이지 로딩을 기다립니다.
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "근태관리")))
            # "근태관리" 링크를 클릭합니다.
            self.driver.find_element(By.LINK_TEXT, "근태관리").click()

            # 프레임이 나타날 때까지 대기합니다.
            WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))
            # 출근 버튼을 클릭합니다.
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".col:nth-child(1) .v-btn__content"))).click()
            print("출근에 성공하였습니다")

        except Exception as e:
            #예외가 발생했을 때 처리할 코드
            print("출근에 실패하였습니다")

        try:
            self.driver.find_element(By.CSS_SELECTOR, ".primary-icon").click()
            self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2)").click()
            print("근무상태변경(업무)가 성공하였습니다")
        except Exception as e:
            #예외가 발생했을 때 처리할 코드
            print("근무상태변경(업무)가 실패하였습니다")

        # try:
        #     # 출근 수정 요소가 나타날 때까지 대기합니다.
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, ".ma-0:nth-child(7)")))
        #     element.click()
        #
        #     # 출근 수정 요소를 클릭한 후에 대기합니다.
        #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "input-84")))
        #
        #     # 출근 수정 요소를 클릭한 후의 나머지 작업을 수행합니다.
        #     self.driver.find_element(By.ID, "input-84").click()
        #     self.driver.find_element(By.CSS_SELECTOR, "#list-item-144-8 .v-list-item__title").click()
        #     self.driver.find_element(By.ID, "input-93").click()
        #     self.driver.find_element(By.CSS_SELECTOR, "#list-item-168-1 .v-list-item__title").click()
        #     self.driver.find_element(By.ID, "input-96").click()
        #
        #     # 스크롤을 이동할 필요가 있는 경우에만 스크롤합니다.
        #     if self.driver.find_element(By.CSS_SELECTOR, ".v-btn--has-bg > .v-btn__content"):
        #         element = self.driver.find_element(By.CSS_SELECTOR, ".v-btn--has-bg > .v-btn__content")
        #         actions = ActionChains(self.driver)
        #         actions.move_to_element(element).perform()
        #
        #     self.driver.find_element(By.ID, "input-96").send_keys("출근 수정입니다")
        #     self.driver.find_element(By.CSS_SELECTOR, ".v-btn--has-bg > .v-btn__content").click()
        #     element = self.driver.find_element(By.CSS_SELECTOR, "body")
        #     actions = ActionChains(self.driver)
        #     actions.move_to_element(element, 0, 0).perform()
        #     print("상태등록 수정(출근)을 성공하였습니다")
        #
        # except Exception as e:
        #     #예외가 발생했을 때 처리할 코드
        #     print("상태등록 수정(출근)을 실패하였습니다 : ", e)