import time

from selenium.webdriver.common.by import By
from locator.Locator import locate

class login:
    def __init__(self, driver):
        self.driver = driver
        self.lc = locate()

    def get_nav_login(self):
        return self.driver.find_element(By.ID, self.lc.nav_login_id)

    def click_nav_login(self):
        return self.get_nav_login().click()

    def get_username(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.lc.uname_id)

    def enter_username(self,username):
        self.get_username().send_keys(username)

    def get_password(self):
        return self.driver.find_element(By.ID, self.lc.pwd_id)

    def enter_password(self,password):
        self.get_password().send_keys(password)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self.lc.button_xpath)

    def click_login_button(self):
        self.get_login_button().click()










    def login_function(self, username,password):
        self.click_nav_login()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(5)
