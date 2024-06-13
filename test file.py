from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_id('ctl00_cphMain_blkLogin_btnGuestLogin').click()
driver.find_element_by_id('ctl00_cphMain_SrchNames1_txtFirmSurName').send_keys("Adam")
datefield = driver.find_element_by_id('ctl00_cphMain_SrchDates1_txtFiledFrom')
ActionChains(driver).move_to_element(datefield).click().send_keys('01012011').perform()
search_btn = driver.find_element_by_id('ctl00_cphMain_btnSearchAll')
ActionChains(driver).move_to_element(search_btn).click().click().perform()