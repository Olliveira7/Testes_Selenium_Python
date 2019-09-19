from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver")

driver.get('https://google.com')

id_pesq = 'tsf'
pesquisa = 'bom dia'
id_btn = 'tsf'
input_id = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(pesquisa)
