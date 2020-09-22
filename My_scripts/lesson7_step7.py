from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    time.sleep(2)

    x=browser.find_element(By.TAG_NAME,"img").get_attribute("valuex")

    browser.find_element(By.ID,"answer").send_keys((calc(x)))

    browser.find_element(By.CSS_SELECTOR,"[type=checkbox]").click()
    browser.find_element(By.ID,"robotsRule").click()
    browser.find_element(By.TAG_NAME,"button").click()





finally:
    time.sleep(7)
    browser.quit()