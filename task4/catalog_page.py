from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CatalogPage:

    def __init__(self, browser: WebDriver) -> None:
        self.driver = browser

    def add_items_to_cart(self, item_names_list):
        items = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
        for item in items:
            if item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text in item_names_list:
                item.find_element(By.CSS_SELECTOR, "button").click()