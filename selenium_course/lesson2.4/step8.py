from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'
link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)

    wait = WebDriverWait(browser, 15).until(
                EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element_by_id("book").click()

    x_element = browser.find_element_by_id('input_value').text
    x = calc(x_element)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(x)

    submit = browser.find_element_by_id('solve').click()


finally:
    time.sleep(10)
    browser.quit()


