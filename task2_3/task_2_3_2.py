from selenium import webdriver
import time
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))  
 
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.trollface")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    button.click()
    
except Exception as ex:
    print(ex)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце фай
