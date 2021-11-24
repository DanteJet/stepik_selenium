import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]
@pytest.mark.parametrize('link', links)
def test_param(browser, link):
    browser.get(link)
    textarea =WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area")))
    answer = math.log(int(time.time()))
    textarea.send_keys(answer)
    button = browser.find_element(By.XPATH, "//button[@class='submit-submission']")
    button.click()
    text = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "pre")))
    assert text.text == "Correct!", text.text