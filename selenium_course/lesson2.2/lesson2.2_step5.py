import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'


try:
    browser = webdriver.Chrome(chromedriver)
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("window.scrollBy(0, 100);")
    button.click()
    assert True



finally:
    time.sleep(30)
    browser.quit()
