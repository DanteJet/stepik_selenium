import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    first_name = browser.find_element_by_css_selector("input[name='first_name']")
    first_name.send_keys("Richard")
    second_name = browser.find_element_by_css_selector("input[name='last_name']")
    second_name.send_keys("Castle")
    city = browser.find_element_by_css_selector("div.form-group:nth-child(3) input")
    city.send_keys("New York")
    country = browser.find_element_by_css_selector("div.form-group:nth-child(4) input")
    country.send_keys("USA")
    button.click()
    time.sleep(3)
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
