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

# Selección de Categoría y Productos

#-------
# Adición de 1er celular al carrito

sleep(2)
# Selección de Categoría de celulares
item = driver.find_element(By.CSS_SELECTOR, "a.list-group-item:nth-child(2)")
item.click()

sleep(2)

item = driver.find_element(By.CSS_SELECTOR, "div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h4:nth-child(1) > a:nth-child(1)")
item.click()

sleep(2)

item = driver.find_element(By.CSS_SELECTOR, "a.btn")
item.click()
item.send_keys(Keys.ENTER)

item = driver.find_element(By.CSS_SELECTOR, "li.nav-item:nth-child(1) > a:nth-child(1)")
item.click()

#--------
# Adición de 2do Celular al carrito

sleep(2)
# Selección de Categoría de celulares
item = driver.find_element(By.CSS_SELECTOR, "a.list-group-item:nth-child(2)")
item.click()

sleep(2)

item = driver.find_element(By.CSS_SELECTOR, "div.col-lg-4:nth-child(2) > div:nth-child(1) > div:nth-child(2) > h4:nth-child(1) > a:nth-child(1)")
item.click()

sleep(2)

item = driver.find_element(By.CSS_SELECTOR, "a.btn")
item.click()
item.send_keys(Keys.ENTER)

item = driver.find_element(By.CSS_SELECTOR, "li.nav-item:nth-child(1) > a:nth-child(1)")
item.click()

#--------
# Adición de 1er laptop

sleep(2)
# Selección de Categoría de laptops
item = driver.find_element(By.CSS_SELECTOR, "a.list-group-item:nth-child(3)")
item.click()

sleep(2)

item = driver.find_element(By.CSS_SELECTOR, "div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h4:nth-child(1) > a:nth-child(1)")
item.click()

sleep(2)

item = driver.find_element(By.CSS_SELECTOR, "a.btn")
item.click()
item.send_keys(Keys.ENTER)

item = driver.find_element(By.CSS_SELECTOR, "li.nav-item:nth-child(1) > a:nth-child(1)")
item.click()

# Adición de 2da laptop
sleep(2)
# Selección de Categoría de laptops
item = driver.find_element(By.CSS_SELECTOR, "a.list-group-item:nth-child(3)")
item.click()

sleep(2)

item = driver.find_element(By.CSS_SELECTOR, "div.col-lg-4:nth-child(2) > div:nth-child(1) > div:nth-child(2) > h4:nth-child(1) > a:nth-child(1)")
item.click()

sleep(2)

item = driver.find_element(By.CSS_SELECTOR, "a.btn")
item.click()
item.send_keys(Keys.ENTER)

item = driver.find_element(By.CSS_SELECTOR, "li.nav-item:nth-child(1) > a:nth-child(1)")
item.click()

#-------------------------------------------------
# Visualización del carrito y compra de objetos
sleep(2)
cart = driver.find_element(By.ID, "cartur")
cart.click()

cart = driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(3)")
cart.click()

# Formulario de Compra
sleep(2)
cart = driver.find_element(By.ID, "name")
cart.send_keys('aeiou')

cart = driver.find_element(By.ID, "country")
cart.send_keys('Parangaticurimicuaro')

cart = driver.find_element(By.ID, "city")
cart.send_keys('Parangaticurimicuaro')

cart = driver.find_element(By.ID, "card")
cart.send_keys('Equisde')

cart = driver.find_element(By.ID, "month")
cart.send_keys('Equisde')

cart = driver.find_element(By.ID, "year")
cart.send_keys('Equisde')

cart = driver.find_element(By.CSS_SELECTOR, "#orderModal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)")
cart.click()

sleep(2)

cart = driver.find_element(By.CSS_SELECTOR, ".confirm")
cart.click()


driver.quit()
