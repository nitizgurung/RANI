import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com/")
nav_login = driver.find_element(By.ID, "login2")
nav_login.click()
uname = driver.find_element(By.ID, "loginusername")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(uname))
uname.send_keys("testmorning")
pwd = driver.find_element(By.ID, "loginpassword")
pwd.send_keys("test123")
button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
button.click()
time.sleep(5)
