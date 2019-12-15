from selenium import webdriver
import time
import math


chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'
link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome(chromedriver)
    browser.get(link)

    button = browser.find_element_by_css_selector("[type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id('input_value').text
    x = calc(x_element)
    input = browser.find_element_by_id('answer').send_keys(x)
    submit = browser.find_element_by_tag_name("button").click()


finally:

    time.sleep(10)
    browser.quit()
