import time
from selenium import webdriver

driver = webdriver.Chrome( executable_path='C:\chromedriver.exe')

driver.get('https://www.google.com/search?q=bom+dia&oq=bom+dia&aqs=chrome..69i57.3513j0j8&sourceid=chrome&ie=UTF-8')
n = 1
while n < 10:
    title = driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[{}]/div/div/div[1]/a/h3/div'.format(n)).text
    print(title)
    n = n + 1

#sucesso