from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox(executable_path='D:/Selenium/WebDriver/geckodriver.exe')
driver.get('https://www.demoblaze.com/index.html')

sleep(2)


# Registro de Usuario
user = driver.find_element(By.ID, 'signin2')
user.click()

sleep(2)

user = driver.find_element(By.ID, "sign-username")
user.send_keys("aeiou12345")

pwd = driver.find_element(By.ID, "sign-password")
pwd.send_keys("aeiou12345")

user.send_keys(Keys.ENTER)

sleep(2)

user.send_keys(Keys.ENTER)


# Inicio de Sesión
user = driver.find_element(By.ID, 'login2')
user.click()

sleep(2)

user = driver.find_element(By.ID, "loginusername")
user.send_keys("aeiou12345")

pwd = driver.find_element(By.ID, "loginpassword")
pwd.send_keys("aeiou12345")

user.send_keys(Keys.ENTER)

