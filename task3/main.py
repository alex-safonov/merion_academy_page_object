from selenium import webdriver
from calculator import Calculator

driver = webdriver.Chrome()
calc = Calculator(driver)
calc.open()

calc.set_delay(5)

calc.press(7)
calc.press("+")
calc.press(8)
calc.press("=")

res = calc.get_result()
print(res)

driver.quit
