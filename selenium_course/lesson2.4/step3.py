from selenium import webdriver
import time


chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'
browser = webdriver.Chrome(chromedriver)

browser.get("http://suninjuly.github.io/wait1.html")
browser.implicitly_wait(5)

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
