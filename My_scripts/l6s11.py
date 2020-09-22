from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector(".first_block .first_class .first").send_keys("Ivan")
    browser.find_element_by_css_selector(".first_block .second_class .second").send_keys("Ivanovich")
    browser.find_element_by_css_selector(".first_block .third_class .third").send_keys("Ivan@lolol.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)