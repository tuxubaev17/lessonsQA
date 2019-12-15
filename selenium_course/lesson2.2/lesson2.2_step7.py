import math
import time
from selenium import webdriver
import os

link = 'http://suninjuly.github.io/file_input.html'
chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'

try:
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("Smolensk")
    current_dir = os.path.abspath(os.path.dirname('/Users/alikhantuxubayev/Documents/environments/selenium_course/'))
    file_path = os.path.join(current_dir, 'a.txt')
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
