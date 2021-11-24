import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMultilanguage:
    def test_items(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = WebDriverWait(browser, 8).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))
        assert button is not None
        time.sleep(10)