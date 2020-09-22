from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link="http://suninjuly.github.io/file_input.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME,"firstname").send_keys("Vasya")
    browser.find_element(By.NAME,"lastname").send_keys("Bibusav")
    browser.find_element(By.NAME,"email").send_keys("vasya@gmail.com")

    current_dir=os.path.abspath(os.path.dirname(__file__))      #находим директорию в которой находимся
    file_path=os.path.join(current_dir,"test_file.txt")         #добовляем к этому пути имя файла

    browser.find_element(By.ID,"file").send_keys(file_path)

    browser.find_element(By.CLASS_NAME,"btn").click()

finally:
    time.sleep(5)

    browser.quit()

