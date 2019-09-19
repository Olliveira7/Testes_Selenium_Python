from selenium import webdriver

driver = webdriver.Firefox(executable_path='C:\geckodriver')

driver.get('https://www.gmail.com')

id_email = 'identifierId'
id_bts_next = 'identifierNext'
email = 'diegoolliveira1999@gmail.com'
input_email = driver.find_element_by_id(id_email)
input_bts_next = driver.find_element_by_id(id_bts_next)
input_email.send_keys(email)
input_bts_next.click()

id_senha = 'password'
id_bts_next2 = 'passwordNext'
senha = 'xxxxxx'
input_senha = driver.find_element_by_id('password')
input_bts_next2 = driver.find_element_by_id(id_bts_next2)
input_senha.send_keys(senha)
input_bts_next2.click()

driver.get('https://www.youtube.com')



