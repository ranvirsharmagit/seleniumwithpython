import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()

driver.get("https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI")

driver.find_element(By.XPATH,"//div[@class='forecast_toggle_arrow']").click()

#dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))    #use Select class for static dropdown
#dropdown.select_by_visible_text("Female")

#driver.find_element(By.XPATH,"").send_keys()
#driver.find_element(By.XPATH,"").send_keys()
#driver.find_element(By.XPATH,"").send_keys()
#driver.find_element(By.XPATH,"").send_keys()
#driver.find_element(By.XPATH,"").send_keys()


time.sleep(5)