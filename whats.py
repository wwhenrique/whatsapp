from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import io
from random import randint

class Whatsapp:
    def __init__(self):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)

    def iniciar(self):
        self.logar_no_site()
        self.enviar_mensagens()

    def logar_no_site(self):
        print('\nDIGITE O NÚMERO DO WHATS, COM CÓDIGO DO PAIS E DDD')
        print('EXEMPLO: +5511987654321\n')
        numero_whats = input('Digite: ')

        print('Acessando site')
        self.navegador.get(f'https://web.whatsapp.com/send?phone={numero_whats}')

        while True:
            sleep(5)
            try:
                side = self.navegador.find_element(By.ID, 'side')

            except NoSuchElementException as e:
                print('Esperando ler QRCode')
            else:
                print('LOGADO')
                sleep(3)
                break

    def ler_arquivo(self):
        arquivo = io.open('arquivo.txt', 'r', encoding="utf8")
        linhas = arquivo.readlines()

        return linhas

    def enviar_mensagens(self):

        try:
            mensagem = self.navegador.find_element(By.CSS_SELECTOR, '[data-testid=conversation-compose-box-input]')
        except NoSuchElementException as e:
            print('Erro')
            self.enviar_mensagens()

        mensagem.click()
        sleep(3)
        linhas_arquivo = self.ler_arquivo()



        count = 0
        while True:
            # envia em ordem
            # for linha in linhas_arquivo:
            #     count+=1
            #     mensagem.send_keys(linha)
            #     mensagem.send_keys(Keys.ENTER)
            #     print(f'Mensagem enviada {count}')
            #     # define tempo de espera para enviar mensagem
            #     sleep(1)

            #envia de maneira aleatoria
            count += 1
            mensagem.send_keys(linhas_arquivo[randint(0, len(linhas_arquivo))])
            mensagem.send_keys(Keys.ENTER)
            print(f'Mensagem enviada {count}')
            # define tempo de espera para enviar mensagem
            sleep(1)


whats = Whatsapp()
whats.iniciar()


