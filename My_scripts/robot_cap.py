from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def robot(x):

    y = x.find_element(By.ID, "input_value").text

    x.find_element(By.ID, "answer").send_keys((calc(y)))

    x.find_element(By.CLASS_NAME, "btn").click()

#мой пример использвования скрипта внутри другого скрипта для заполнения значения поля посчитаное по формуле
#используется в l9_s4,l9_s6