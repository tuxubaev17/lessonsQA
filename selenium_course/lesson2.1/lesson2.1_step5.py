import math
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/math.html'
chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'

try:
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[value='robots']")
    radiobutton.click()
    submit = browser.find_element_by_class_name('btn')
    submit.click()


finally:
    time.sleep(30)
    browser.quit()
