from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link="http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    x=browser.find_element(By.ID,"input_value").text

    browser.find_element(By.ID,"answer").send_keys((calc(x)))

    browser.find_element(By.CSS_SELECTOR,"[type=checkbox]").click()
    browser.find_element(By.ID,"robotsRule").click()
    browser.find_element(By.TAG_NAME,"button").click()




finally:
    time.sleep(7)
    browser.quit()