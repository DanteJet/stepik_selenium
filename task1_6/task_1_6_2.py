import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")

first_name = browser.find_element_by_tag_name("input")
first_name.send_keys("Richard")
second_name = browser.find_element_by_name("last_name")
second_name.send_keys("Castle")
city = browser.find_element_by_class_name("city")
city.send_keys("New York")
country = browser.find_element_by_id("country")
country.send_keys("USA")
button.click()
time.sleep(3)

time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()
