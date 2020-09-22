from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import robot_cap

link="http://suninjuly.github.io/redirect_accept.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME,"btn").click()

    new_window=browser.window_handles[1]

    browser.switch_to.window(new_window)

    robot_cap.robot(browser)

    alert=browser.switch_to.alert
    print(alert.text)

finally:
    time.sleep(2)
    browser.quit()