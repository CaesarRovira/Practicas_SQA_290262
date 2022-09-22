from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox(executable_path='D:/Selenium/WebDriver/geckodriver.exe')
action = AC(driver)

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

sleep(2)

#box = driver.find_element(By.ID, 'box1')
#tgt = driver.find_element(By.ID, 'box101')

#action.drag_and_drop(box, tgt).perform()

for i in range(0,7):
    txt1 = f'box{i+1}'
    txt2 = f'box10{i+1}'

    box = driver.find_element(By.ID, txt1)
    tgt = driver.find_element(By.ID, txt2)

    action.drag_and_drop(box, tgt).perform()

