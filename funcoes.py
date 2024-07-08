from selenium import webdriver                                              # Biblioteca Selenium é para pegar informações na tela do navegador
from selenium.webdriver.common.by import By
import time                                                                 # Biblioteca Time é para controlar o tempo entre uma tela e outra
import os                                                                   # Biblioteca OS para naver entre diretorios do PC
import tkinter as tk
from tkinter import messagebox as mb

pasta = r'C:\Users\nando.DESKTOP-599MFJB\OneDrive\Área de Trabalho\Automatizar\3 zipa e enviar por whats OK' # endereço do diretorio que os arquivos a ser enviado vai está
contato = "https://web.whatsapp.com/send?phone=5511945180799&text= "        # Essa variaveu está com o endereço para ir direto ao numero desejado

def Contatos(): # Ciar uma lista de contatos para enviar os arquivos de forma mais fascil 
    pass


def Arquivos(diretorio):                                                    # Função para pegar o caminho completo dos arquivos na pasta
    caminhoCompleto = []                                                    # Criei uma lista para salvar o caminho completo do arquivo
    for pasta, subpasta, arquivos in os.walk(diretorio):                    # gravo o caminho ate os arquivos que quero
        for nomeArquivo in arquivos:                                        # Pego o nome do arquivo dentro da pasta
            caminhoCompleto.append(os.path.join(pasta,nomeArquivo))         # Junto o caminho da pasta com o nome do arquivo envio para lista criada
    return caminhoCompleto                                                  # Sempre que essa função for chamada ela vai retorna a lista criada

def EnviaWhatsapp(contatos,CaminhoCompletoPasta):                                 # Essa função entra no whatsapp para enviar os arquivos
    qntArquivos = 0                                                         # Criei a variavel para contar quantos arquivos foi enviado
    if Arquivos(CaminhoCompletoPasta) == []:                                # Verificação se a lista estiver vazia
        print('Não tem arquivos na pasta')                                  # Se sim imprime a mensagem não tem arquivos na pasta
        return qntArquivos                                                  # E retorna retorna a variavel quantidade de arquivo igual a zero
    else:                                                                   # Se tiver arquivos dentro da pasta
        driver = webdriver.Edge()                                           # Escolho o navegador opcional
        driver.get(contatos)                                                # Peço para o navegador abrir no contato escolhido com a variavel contato
        while len(driver.find_elements(By.XPATH,'//*[@id="side"]/span/div/div')) <1:    # Espera até esse ele mento aparecer na tela do navegador
            time.sleep(1)                                                                     # Otempo para verificar novamente se o elemento apareceu na tela
        time.sleep(1)                                                                         # Depois que o elemento apareceu aguarde mais 1 segundo para carregar tudo
        for arquivo in Arquivos(CaminhoCompletoPasta):                      # Pego arquivo por arquivo para ser enviado para o contato
            time.sleep(3)                                                   # Aguardo 3 segundo
            driver.find_element(By.XPATH,                                   # Clico no botão de anexa arquivos
                                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
            driver.find_element(By.XPATH,                                   # Depois de clicar no botão aparece o input eu pego o caminho dele e coloco o caminho do arquivo
                                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li/div/input').send_keys(arquivo)
            time.sleep(1)                                                   # Aguardo 1 segundo
            driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()  # Clico em enviar
            qntArquivos += 1                                                # Adiciono 1 na variavel quantidade de arquivos
        time.sleep(5)                                                       # Aguardo 5 segundo
        return qntArquivos                                                  # Retorno a variavel com a quantidade de arquivos enviado


if __name__ =='__main__':
   

    '''      Usee o arquivo chamado ZiparArquivos para enviar os arquivos depois de compactar as pastas           '''