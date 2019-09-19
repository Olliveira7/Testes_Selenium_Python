from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver")
driver.get('https://www.facebook.com')

id_login = 'email' #essa variável é pra descobrir os elementos de tela em q vai ser buscado
id_pass = 'pass'    # a mesma coisa do anterior
id_btn = 'loginbutton'  # esse é o do botão então os cuidados são diferenciados, a lembrar que essa busca está no id
login = 'diegouniver1999@gmail.com'  #essa variável é pra receber os valores em que eu quero inserir nos campos
passs = 'minicurso12345'
input_login = driver.find_element_by_id(id_login)   # aqui ele vai buscar os elementos de tela que estiverem na varivel
input_pass = driver.find_element_by_id(id_pass)
input_btn = driver.find_element_by_id(id_btn)
input_login.send_keys(login)    # a função send_key serve para enviar algo
input_pass.send_keys(passs)
input_btn.click()   # essa função serve para clicar em um certo botão
driver.quit()
