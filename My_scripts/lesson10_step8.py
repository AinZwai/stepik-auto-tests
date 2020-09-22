from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:

    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    botton1=browser.find_element(By.ID, "book")

    WebDriverWait(browser,15).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))

    botton1.click()

    botton2=browser.find_element(By.ID,"solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);",botton2)

    y = browser.find_element(By.ID, "input_value").text

    browser.find_element(By.ID, "answer").send_keys((calc(y)))

    botton2.click()
finally:
    time.sleep(7)
    browser.quit()
