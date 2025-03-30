import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com/")
try:
    nav_login = driver.find_element(By.ID, "login2")
    nav_login.click()
    uname = driver.find_element(By.ID, "loginusername")
    uname.send_keys("testmorning")
    pwd = driver.find_element(By.ID, "loginpassword")
    pwd.send_keys("test123")
    button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    button.click()
    time.sleep(5)
except ElementNotInteractableException:
    print("This is from Element Not Interactable")
    driver.implicitly_wait(10)
    uname = driver.find_element(By.ID, "loginusername")
    uname.send_keys("testmorning")
    pwd = driver.find_element(By.ID, "loginpassword")
    pwd.send_keys("test123")
    button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    button.click()
    time.sleep(5)
except Exception as e:
    print(e)
