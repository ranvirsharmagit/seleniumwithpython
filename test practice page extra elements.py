import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#for checkbox
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']") #this way we did because if we are unable to find a specific checkboc xpath then we checl full list of checkbox option

print(len(checkboxes))  #by this we get how many checkbox available

for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option2":  #through this we will find value is equal to option2 then click
        checkbox.click()
        assert checkbox.is_selected()  # this to check if check box is selected or not "is_selected" is a method
        break

#for radio button
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton") #use find_elements(plural) when you have list and aftr list you select one option
radiobuttons[2].click() #we are not use loop because we presume that we know the radiobutton list series
assert radiobuttons[2].is_selected()

#for hiden fielda
assert driver.find_element(By.ID,"displayed-text").is_displayed() #by this assert we check that field is diplayed
driver.find_element(By.ID,"hide-textbox").click() #by this we click on the hide button
assert not driver.find_element(By.ID,"displayed-text").is_displayed() # by this we can check that is not displayed by "assert not"


name = "ranvir"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)

driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert  #to inform about the popup alert
alerttexxt = alert.text
print(alerttexxt) # to print the allert popup text

assert name in alerttexxt #to check alert name variable is in popup or not
alert.accept() #to click OK






time.sleep(2)