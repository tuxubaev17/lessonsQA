import math
import time
from selenium import webdriver

link = 'http://SunInJuly.github.io/execute_script.html'
chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)


    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()
    radiobutton = browser.find_element_by_css_selector("[value='robots']").click()
    sunbint = browser.find_element_by_class_name("btn").click()


finally:
    time.sleep(5)
    browser.quit()
