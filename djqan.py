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

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    # self.driver.get("https://nstaging.daouoffice.com/app/att_timeline")
    # self.driver.set_window_size(1552, 840)
    # self.driver.switch_to.default_content()
    # self.driver.find_element(By.CSS_SELECTOR, ".on .menu").click()
    # self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, ".primary-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2)").click()
  