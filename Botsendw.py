#from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
import time

#Abre o Chrome
driver = webdriver.Chrome('./chromedriver')
driver.get('https://web.whatsapp.com/') #abre o site whatsapp 

#espera voce logar por tempo indeterminado.
while len(driver.find_elements_by_id('side')) <1:
    time.sleep(1)

#Lista de contato ou grupo
contatos = ['Meu', 'Cida']

#As mensagens que sera enviada
msg1 = 'Boa noite '
msg2 = ' Deus abençoe.'

#Passar o caminho do arquivo 
arquivo = "/home/prado/Bots_python/Bot_whatsapp/imag.png"

#Pesquisa o Contato ou Grupo
def buscar_contato(contato):
    pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    pesquisa.click()
    pesquisa.send_keys(contato)
    pesquisa.send_keys(Keys.ENTER)

#Envia a mensagem
def enviar_mensagem(msg1, msg2):
    mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    mensagem[1].click()
    mensagem[1].send_keys(str(msg1) + str(contato) + str(msg2))
    mensagem[1].send_keys(Keys.ENTER)
    time.sleep(3)

#Onde vai enviar o arquivo e a mensagem
def enviar_midia(arquivo):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(arquivo)
    time.sleep(4)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()    

#Envia as mensagens para todos os seus contatos da lista 
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(msg1,msg2)       
    enviar_midia(arquivo) 
    time.sleep(1)
driver.close()