import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("ranvir")  #id, classname, name, cssselector, xpath, linktext
#xpath = //tagname[@attribute='value']
#cssselector = tagname[attribute ='value'] or #id or .classname
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("ranvir@gmail.com")
driver.find_element(By.XPATH,"//input[@name='bday']").send_keys('30081986')
time.sleep(5)