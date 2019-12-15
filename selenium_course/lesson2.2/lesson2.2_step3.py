import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'
chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'

def sum(x,y):
    total = int(x) + int(y)
    return total


try:
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)

    x_element = browser.find_element_by_id('num1').text
    y_element = browser.find_element_by_id('num2').text
    answ = sum(x_element, y_element)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(answ))

    submit = browser.find_element_by_class_name('btn').click()



finally:
    time.sleep(30)
    browser.quit()
