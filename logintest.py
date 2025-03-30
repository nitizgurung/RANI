import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from page.LoginPage import login


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        self.lp = login(self.driver)

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

    def test_login(self):
        self.lp.login_function("testmorning", "test123")




        expected_result = "Welcome testmorning"
        actual_result = self.driver.find_element(By.ID, "nameofuser").text
        self.assertEqual(expected_result, actual_result, "They must not be same user")

    def test_login_negative(self):
        self.lp.login_function("testmorning", "password")
        self.driver.switch_to.alert.accept()



if __name__ == '__main__':
    unittest.main()
