from selenium import webdriver
from auth_page import AuthPage
from catalog_page import CatalogPage
from cart_page import CartPage

driver = webdriver.Chrome()
driver.implicitly_wait(10)

auth = AuthPage(driver)
auth.open()
auth.auth("standard_user", "secret_sauce")

catalog = CatalogPage(driver)

catalog.add_items_to_cart(["Sauce Labs Backpack","Sauce Labs Bolt T-Shirt","Sauce Labs Onesie"])

cart = CartPage(driver)
cart.open()
total = cart.checkout().set_contacts("Иван","Иванов","123456").get_total()

print(total)

driver.quit()
