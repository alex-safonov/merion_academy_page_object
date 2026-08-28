from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from contact_page import ContactPage

class CartPage:

    def __init__(self, browser: WebDriver) -> None:
        self.driver = browser

    def open(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        return ContactPage(self.driver)
    