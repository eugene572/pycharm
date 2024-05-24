# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestEx1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_ex1(self):
    self.driver.get("https://portal.daou.co.kr/login")
    time.sleep(5)
    self.driver.set_window_size(1011, 840)
    time.sleep(5)
    self.driver.find_element(By.ID, "password").click()
    time.sleep(5)
    self.driver.find_element(By.ID, "login_submit").click()
    time.sleep(5)
    self.driver.close()

    time.sleep(5)
  
