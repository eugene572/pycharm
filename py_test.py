from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestEx1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # implicity_wait를 10초로 설정합니다.
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_ex1(self):
        self.driver.get("https://portal.daou.co.kr/login")
        self.driver.set_window_size(1011, 840)
        self.driver.find_element(By.ID, "username").send_keys("yoojin1216")
        self.driver.find_element(By.ID, "password").send_keys("suji10815!")
        self.driver.find_element(By.CSS_SELECTOR, ".login_box:nth-child(1)").click()
        self.driver.find_element(By.ID, "login_submit").click()
        element = self.driver.find_element(By.ID, "login_submit")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).move_by_offset(0, 0).perform()
        self.driver.close()