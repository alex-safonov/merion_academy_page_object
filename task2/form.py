from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class Form:

    def __init__(self, browser: WebDriver) -> None:
        self.driver = browser

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def set_value_for(self, field_name, field_value):
        self.driver.find_element(By.CSS_SELECTOR, f"[name={field_name}]").send_keys(field_value)

    def send_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    def get_css_property_for(self, selector, property_name):
        return self.driver.find_element(By.CSS_SELECTOR, selector).value_of_css_property(property_name)
    