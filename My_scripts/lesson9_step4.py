from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import robot_cap

link="http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME,"btn").click()

    aler=browser.switch_to.alert        #переключиться на окно с alert
    aler.accept()                       #принять его с помощью команды accept()

    robot_cap.robot(browser)

finally:
    time.sleep(7)
    browser.quit()
