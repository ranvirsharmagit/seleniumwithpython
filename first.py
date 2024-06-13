import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://facebook.com") # for opnen this link
driver.maximize_window() #to maximize the window
print(driver.title) #to print page title
print(driver.current_url) #for print link on result




time.sleep(2)