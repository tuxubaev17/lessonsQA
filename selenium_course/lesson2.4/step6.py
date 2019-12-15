from selenium import webdriver
import time

link = 'http://suninjuly.github.io/cats.html'
chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'
browser = webdriver.Chrome(chromedriver)

browser.get(link)
browser.implicitly_wait(5)

browser.find_element_by_id("button")

time.sleep(5)

browser.quit()