import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.PARTIAL_LINK_TEXT,"password").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("ranvir.sharma088@gmail.com") #create xpath through parent to child class using /
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("ranvir123") #create css same way using class but in this use space instead of slash
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("ranvir123")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()




time.sleep(5)
