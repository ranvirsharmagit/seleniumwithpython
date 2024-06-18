import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")

time.sleep(5)
count = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a") #crate css for all option available in drop down to check in series and find desirable keyword

print(len(count))  #to print how many option available aftr enter "IND" in field

for country in count:             #this program to search all option available and select the right keyword to enter
     if country.text == "India":
         country.click()
         break    # use to stp the loop

#print(driver.find_element(By.ID,"autosuggest").text) #use when first time without any change you need to check but if page is refreshed then nothing print
print(driver.find_element(By.ID,"autosuggest").get_attribute("value")) #to record and print the valuewhich is entered after select from the list

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India" # "assert" to check "India" is appear on field or Not


