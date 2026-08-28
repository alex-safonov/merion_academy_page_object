from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from final_page import FinalPage

class ContactPage:

    def __init__(self, browser: WebDriver) -> None:
        self.driver = browser

    def set_contacts(self, firstname, lastname, zipcode):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(firstname)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(lastname)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zipcode)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        return FinalPage(self.driver)