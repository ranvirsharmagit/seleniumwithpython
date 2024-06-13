import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("ranvir")  #id, classname, name, cssselector, xpath, linktext
#xpath = //tagname[@attribute='value']
#cssselector = tagname[attribute ='value'] or #id or .classname
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("ranvir@gmail.com")
#driver.find_element(By.XPATH,"//input[@name='bday']").is_selected(30/08/1986) issue with select date
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("ranvir")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear() #add index number in the end of xpth if there multipule elemnt available with same
message = driver.find_element(By.CLASS_NAME,"alert-success").text #to print the pop message
print(message)
assert "success" in message  #to check the "Success" keyword available in pop message

time.sleep(2)