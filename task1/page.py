from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class Page:

    def __init__(self, browser: WebDriver) -> None:
        self.driver = browser

    def open(self):
        self.driver.get("http://uitestingplayground.com/textinput")

    def get_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#newButtonName")

    def get_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#updatingButton")

    # строгий подход к Page Object:
    def set_button_name(self, new_name:str):
        self.get_input().send_keys(new_name)
        self.get_button().click()

    def get_button_text(self):
        return self.get_button().text
