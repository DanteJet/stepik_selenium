import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        elements = browser.find_elements(By.CSS_SELECTOR, "input:required")
        i = 1
        for element in elements:
            element.send_keys("Answer" + str(i))
            i = i + 1

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        # Поиск элементов
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_class input:required")
        last_name = browser.find_element(By.CSS_SELECTOR, "div.second_class input:required")
        email = browser.find_element(By.CSS_SELECTOR, "div.third_class input:required")
        # Заполнение полей
        first_name.send_keys("Richard")
        last_name.send_keys("Castle")
        email.send_keys("castle@example.com")
        # Отправка формы
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Получение текста по результатам отправки формы
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()