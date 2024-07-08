import os
from dataclasses import dataclass
from tkinter.filedialog import askdirectory
import shutil
from zipfile import ZipFile
import pandas as pd
import gspread
from os.path import basename
from funcoes import EnviaWhatsapp



@dataclass                          # Classe Produto é para criar uma pasta com o mesmo nome da imagem e colocar as imagens dendro
class Automacao:
        nome= []
        caminho= []
        nomepasta = []
        contato = "https://web.whatsapp.com/send?phone=5511945180799&text= " 


        def Primeiro_passo(self,):                      # Função primeiro passo verifica se tem imagens na pasta para começar
            self.pasta = askdirectory(title="Selecione a pasta com as imagens.")# Pede para selecionar a pasta onde está as imagen e retorna o caminho
            if not os.listdir(self.pasta):              # Se estiver sem imagens na pasta vai informar que não tem imagens
                    print('Não tem imagens na pasta')
            else:                                       # Se não vai entra na pasta pegar o nome das imagens e criar o caminho
                                                        # Canectando com a Google Planilha
                CODE = '18wbCkghmTBL2MG7uGef9_yHIxlKOz29qxB0WvZU5ofY'
                gc = gspread.service_account(filename='key.json')
                sh = gc.open_by_key(CODE)
                ws = sh.worksheet('Página1')
                                                        # Transformando em um DataFrame e transformando a 2 linha no cabeçalho
                Planilha = pd.DataFrame(ws.get_all_values())
                Planilha.columns = Planilha.iloc[1]
                Planilha = Planilha[1:]
                Planilha = Planilha.drop(1)
                Planilha = Planilha.reset_index(drop=True)

                                                        # Escolher onde vai crar as pastas e pegar o caminho
                onde_vai_pastas = askdirectory(title=f"Selecione onde podemos criar e enviar as {len(os.listdir(self.pasta))} imagens encontradas.")

                                                        # Na pasta onde está as imagens vai pegar o nome e o caminho delas
                for pasta, subpasta, arquivo in os.walk(self.pasta):
                        b = [var for var in arquivo]
                        for sub in b:
                                self.nome.append(sub)
                        for arq in arquivo:
                                self.caminho.append(f'{pasta}/{arq}')
                        a = [var for var in arquivo]
                        for su in a:
                                self.nomepasta.append(su.split('.')[0])
                                                        # Pegando o caminho e o nome das duas imagens que tem que estar em todas as pastas
                copias = r'C:\Users\nando.DESKTOP-599MFJB\OneDrive\Área de Trabalho\Automatizar\copias'
                doisarquivos = os.listdir(copias)
                                                        # Vai criar a pasta com o mesmo nome dos arquivos
                os.chdir(onde_vai_pastas)
                n = 0
                for pas in self.nome:
                    nomePlanilha = [var for var in self.Planilha[self.Planilha['Pasta/Nome do Arquivo'] == pas][
                        'Nome do produto'].values]
                    novapasta = f'Can - {nomePlanilha[0]}' # Nome da nova pasta
                    os.mkdir(novapasta)                 # Criar a nova pasta para envia os arquivos que vem do google Planilhas
                    caminhoPasta = f'{onde_vai_pastas}/{novapasta}'
                    os.rename(self.caminho[n], (f'{caminhoPasta}/{pas}'))
                                                        # copiando as duas imagens dentro da nova pasta
                    shutil.copyfile(os.path.join(copias,doisarquivos[0]),os.path.join(caminhoPasta,doisarquivos[0]))
                    shutil.copyfile(os.path.join(copias,doisarquivos[1]),os.path.join(caminhoPasta,doisarquivos[1]))
                    n+=1

        def Segundo_passo(self):
            # Entra na pasta Criar pasta ver se tem arquivos e salvar
            Arquivos = askdirectory(title="Selecione o caminho das Pastas prontas.")
            if os.listdir(Arquivos) == []:
                print('Pasta não tem arquivos')
            else:
                # Salvei o nome das Pastas
                nomepastas = [var for var in os.listdir(Arquivos)]
                zip_vai = askdirectory(title=f"Selecione a pasta onde vai os {len(nomepastas)} arquivos zipados.")
                if os.listdir(zip_vai) != []:
                    print('Esvazie a pasta onde vai colocar os arquivos zip primeiro')
                else:
                    Qnt = 0
                    for nomeSubpasta in nomepastas:
                        os.chdir(zip_vai)
                        with ZipFile(f'{nomeSubpasta}.7z', 'w') as zip:
                            caminhoPastaZip = os.path.join(Arquivos,nomeSubpasta)
                            arqParaZipar = os.listdir(caminhoPastaZip)
                            for arq in arqParaZipar:
                                arq2 = os.path.join(caminhoPastaZip,arq)
                                zip.write(arq2, basename(arq2))
                                Qnt+=1
                    print('Você compactou {Qnt} agora vamos enviar por Whatsapp')
                    EnviaWhatsapp(self.contato,zip_vai)

if __name__ == '__main__':
     play = Automacao()
     play.Segundo_passo()