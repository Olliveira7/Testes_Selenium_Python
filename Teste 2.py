
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\geckodriver.exe')

end = ""
N = '0'

for c in range(0,6):
    N = str(int(N)+10)
    end = ('https://www.google.com/search?q=chat.whatsapp.com&ei=3uukXJilCrSr5OUPr9Sn0Aw&start=10&sa=N&ved=0ahUKEwiYjLuAuLThAhW0FbkGHS_qCcoQ8tMDCIsB&biw=1680&bih=977')
    end = end.replace('10',N)
    driver.get(end)
    div = driver.find_element_by_id('rso')
    links = div.find_elements_by_tag_name('a')
    for link in links:
        print(link.get_attribute('href'))