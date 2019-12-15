import math
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/get_attribute.html'
chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)


    x_element = browser.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(x_element)
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[value='robots']")
    radiobutton.click()
    submit = browser.find_element_by_class_name('btn')
    submit.click()


finally:
    time.sleep(30)
    browser.quit()
