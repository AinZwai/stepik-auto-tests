#переход по другой ссылке и работа по ней. источник: https://selenium-python.com/hyperlink

from selenium import webdriver
import time

try:
    link="https://yandex.ru/"
    browser=webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

#на кнопке есть атребут href, который ведет на другую ссылку. команда get_attribute позволяет получить значение атребута

    new_window = browser.find_element_by_css_selector("div.rows-wrapper [role=form] [role=button]").get_attribute("href")
    browser.get(new_window)

    time.sleep(3)

    browser.find_element_by_css_selector("input[name=login]").send_keys("Ivan")

    button = browser.find_element_by_css_selector("[type=submit]")
    button.click()

finally:

    time.sleep(10)
    browser.quit()

