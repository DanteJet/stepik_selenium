import time
import math
from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element_by_tag_name("input")
first_name.send_keys("Richard")
second_name = browser.find_element_by_name("last_name")
second_name.send_keys("Castle")
city = browser.find_element_by_class_name("city")
city.send_keys("New York")
country = browser.find_element_by_id("country")
country.send_keys("USA")
button = browser.find_element_by_xpath("//button[text()='Submit']")
button.click()
time.sleep(3)

time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()
