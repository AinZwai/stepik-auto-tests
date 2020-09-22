from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select                    # спец. инструмент для выбора элемента из списка
import time                                                         # можно и без него с помощью find_element().click()
                                                                    # но так не очень удобно
link="http://suninjuly.github.io/selects1.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)

    x=browser.find_element(By.ID,"num1").text
    y=browser.find_element(By.ID,"num2").text

    select = Select(browser.find_element(By.TAG_NAME, "select"))  # создание переменной класса Select

    select.select_by_value(str(int(x)+int(y)))

    browser.find_element(By.CLASS_NAME,"btn").click()

finally:
    time.sleep(5)
    browser.quit()
