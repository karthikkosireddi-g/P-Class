from selenium import webdriver
from selenium.webdriver.common.by import By

myD1 = webdriver.Chrome(executable_path="C:\\Users\\jcady\\PycharmProjects\\chromedriver.exe")

myD1.get("https://mortgagecalculator.org/")
myD1.find_element_by_id("homeval").send_keys("433300")


myD1.get("https://www.pse.com/")

myD1.get("https://10.232.53.39/php/login.php")
