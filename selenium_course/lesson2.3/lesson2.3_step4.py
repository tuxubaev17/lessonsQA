import time
from selenium import webdriver
import math

link = 'http://suninjuly.github.io/alert_accept.html'
chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)

    button = browser.find_element_by_tag_name('button').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id('input_value').text
    x = calc(x_element)
    input = browser.find_element_by_id('answer').send_keys(x)
    submit = browser.find_element_by_tag_name("button").click()



finally:
    time.sleep(10)
    browser.quit()
