from selenium import webdriver
from selenium.webdriver.common.by import By
from page import Page
#import time

driver = webdriver.Chrome()
page = Page(driver)

# упрощённый подход к Page Object:
# page.open()
# page.get_input().send_keys("Merion")
# page.get_button().click()
# txt = page.get_button().text

# строгий подход к Page Object:
page.open()
page.set_button_name("Merion7")
#time.sleep(3)
txt = page.get_button_text()

print(txt)

driver.quit