import time
from selenium import webdriver

driver = webdriver.Chrome( executable_path='C:\chromedriver.exe')

driver.get('https://www.google.com.br/search?client=firefox-b-d&q=chat.whatsapp.com')

time.sleep(15)

div = driver.find_element_by_id('rso')

links = div.find_elements_by_tag_name('a')

for link in links:
    print(link.get_attribute('href'))