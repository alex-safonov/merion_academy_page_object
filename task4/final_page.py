from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class FinalPage:

    def __init__(self, browser: WebDriver) -> None:
        self.driver = browser

    def get_total(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    