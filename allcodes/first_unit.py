import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

    def test_login(self):
         driver = self.driver
         nav_login = driver.find_element(By.ID, "login2")
         nav_login.click()
         driver.implicitly_wait(10)
         uname = driver.find_element(By.ID, "loginusername")
         uname.send_keys("testmorning")
         pwd = driver.find_element(By.ID, "loginpassword")
         pwd.send_keys("test123")
         button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
         button.click()
         time.sleep(5)
         expected_result = "Welcome testmorning"
         actual_result = driver.find_element(By.ID, "nameofuser").text
         self.assertEqual(expected_result, actual_result, "They must not be same user")










if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()
