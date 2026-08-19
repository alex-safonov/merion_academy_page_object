from selenium import webdriver
from form import Form
#import time

driver = webdriver.Chrome()
form = Form(driver)
form.open()

form.set_value_for("first-name", "Иван")
form.set_value_for("last-name", "Петров")
form.set_value_for("address", "Ленина, 55-7")
form.set_value_for("city", "Москва")
form.set_value_for("job-position", "QA")
form.set_value_for("country", "Россия")
form.set_value_for("company", "Merion")

form.send_form()

zipcode = form.get_css_property_for("#zip-code", "background-color")
email = form.get_css_property_for("#e-mail", "background-color")
phone = form.get_css_property_for("#phone", "background-color")

print(zipcode, email, phone)

driver.quit