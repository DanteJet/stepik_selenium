from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
 
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    sums = num1 + num2
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sums))
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

177486
наход
