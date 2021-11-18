from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    treasure = browser.find_element_by_xpath("//img[@id='treasure']")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    robot = browser.find_element_by_id("robotsRule")
    robot.click()
    # Отправка формы    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
except Exception as ex:
    print(ex)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце фай
