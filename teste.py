from selenium import webdriver
from selenium.webdriver.comon.keys import Keys
q = raw_input("Enter the search query")
q = q.replace(' ', '')
browser = webdriver.Firefox()
body = browser.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')
counter = 0
for i in range(0,20):
    browser.get("https://www.google.com/search?q=" + q + "&start=" + str(counter))
    body = browser.find_element_by_tag_name("body")
    if "thetaranights" in body.text:
        browser.find_element_by_xpath('//a[starts-with(@href,"http://www.thetaranights.com")]').click()
        break
    counter += 10


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http:google.com.br'
        self.search_bar = 'lst-ib'

    def navigate(self):
        self.driver(self.url)

    def search(self):

ff = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\geckodriver.exe')
g = Google(ff)