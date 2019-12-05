from selenium import webdriver
from selenium.webdriver.common.by import By

myD1 = webdriver.Chrome(executable_path="C:\\Users\\jcady\\PycharmProjects\\chromedriver.exe")

vURL = "https://10.232.53.39/php/login.php"
vUN = "p-class"
vPWD = "Password01"
print("Automation Testing through Selenium")

myD1.get(vURL)
myD1.find_element_by_id("user").send_keys(vUN)
myD1.find_element_by_id("passwd").send_keys(vPWD)

uNameLabel = "//*[@id='trInitName']/td[1]/label"

# print (myD1.find_element_by_xpath(uNameLabel).get_attribute("text"))

myD1.find_element_by_name("ok").click()

# //*[@id="ext-gen93"]