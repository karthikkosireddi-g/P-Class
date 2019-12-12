from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

myD1 = webdriver.Chrome(executable_path="C:\\Users\\jcady\\PycharmProjects\\chromedriver.exe")
myD1.implicitly_wait(15) # wait for the poge to load before throwing error

vURL = "https://10.232.53.39/php/login.php"
vUN = "p-class"
vPWD = "Password01"
print("Automation Testing through Selenium")

myD1.get(vURL)

uNameLabel = "//*[@id='trInitName']/td[1]/label"
print (myD1.find_element_by_xpath(uNameLabel).text)
myD1.maximize_window()
myD1.find_element_by_id("user").send_keys(vUN)
myD1.find_element_by_id("passwd").send_keys(vPWD)
myD1.find_element_by_name("ok").click()

# print (myD1.find_element_by_xpath("//*[@id='ext-gen93']").text)

# time.sleep(20)
WebDriverWait(myD1, 20, poll_frequency=1).until(ec.visibility_of_element_located((By.ID, "ext-gen353")))
myD1.find_element_by_id("ext-gen353").click()

try :
    myD1.find_element_by_id("ext-gen388").click()
except :
    print("Didnt find the pop-up for Global Find")
# myD1.find_element_by_id("panorama").click()
# myD1.find_element_by_link_text("Password Profiles").click()

#//*[@id="ext-gen52"]/tbody[1]/tr[1]/td[1]/a/span

myD1.find_element_by_id("ext-gen85").click()
myD1.find_element_by_id("ext-comp-1292").send_keys("ip-")
myD1.find_element_by_id("ext-gen353").click()

time.sleep(5)

print (myD1.find_element_by_xpath("//*[@id='ext-gen52']/tbody[1]/tr[1]/td[1]/a/span"))
print("END OF TEST")