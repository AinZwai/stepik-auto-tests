from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link="http://SunInJuly.github.io/execute_script.html"

def f(x):
   return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get(link)

    x=browser.find_element(By.ID,"input_value").text
    browser.find_element(By.ID,"answer").send_keys(f(x))

    browser.find_element(By.CSS_SELECTOR, "[type=checkbox]").click()

    botton1=browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);",botton1)
    botton1.click()

    browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(5)
    browser.quit()





