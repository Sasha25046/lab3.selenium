
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def test_selenium_form():
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        print("Відкрито сторінку тестування...")

        print("\nЗапуск сценарію 1: Текстове введення...")
        text_input = driver.find_element(By.NAME, "my-text")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button")

        text_input.send_keys("Привіт, Selenium!")
        submit_button.click()

        message = driver.find_element(By.ID, "message").text
        assert "Received!" in message
        print("Сценарій 1 успішний: Форма відправлена.")

        driver.back()

        print("\nЗапуск сценарію 2: Checkbox та Radio...")
        checkbox = driver.find_element(By.ID, "my-check-2") 
        radio = driver.find_element(By.ID, "my-radio-2")     

        checkbox.click()
        radio.click()

        assert checkbox.is_selected()
        assert radio.is_selected()
        print("Сценарій 2 успішний: Елементи вибрано.")

        print("\nЗапуск сценарію 3: Dropdown...")
        dropdown = driver.find_element(By.NAME, "my-select")
        dropdown.click()
        
        option_two = driver.find_element(By.XPATH, "//option[@value='2']")
        option_two.click()

        assert option_two.is_selected()
        print("Сценарій 3 успішний: Опцію в списку змінено.")

    except Exception as e:
        print(f"Помилка під час виконання тестів: {e}")
    finally:
        driver.quit()
        print("\nТестування завершено, браузер закрито.")

if __name__ == "__main__":
    test_selenium_form()


