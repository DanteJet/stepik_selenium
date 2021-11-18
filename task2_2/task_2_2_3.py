from selenium import webdriver
import time
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))  
 
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    file_upload = browser.find_element_by_xpath("//input[@id='file']")
    first_name = browser.find_element_by_xpath("//input[@name='firstname']")
    last_name = browser.find_element_by_xpath("//input[@name='lastname']")
    email = browser.find_element_by_xpath("//input[@name='email']")
    
    first_name.send_keys("Richard")
    last_name.send_keys("Castle")
    email.send_keys("castle@example.com")
    file_upload.send_keys(file_path)
    
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
    
except Exception as ex:
    print(ex)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце фай
