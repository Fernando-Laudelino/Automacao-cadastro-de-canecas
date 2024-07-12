># Automatizar o cadastro de produtos 
>> Tenho que pegar a imagem dentro de uma drive compartilhado, salvar a imagem no meu PC criar uma pasta com o nome da imagem.<br>
Entra no site colocar a imagem na caneca e criar duas imagens e um video da caneca girando em 360 graus, pegar as 2 imagens e o video e colocar dentro da pasta nova criada, compactar e enviar para uma outra pessoa para tratar o tamanho das imagens e adicionar mais 4 imagens novoas.<br>
Vou receber o arquivo compactado com o mesmo nome, salvo a pasta compactada dentro da pasta e descompacto ela com as 6 imagens e o video, 
>---
>>##  **classe automação** 
>>
>> ### Variaveis da Classe.
>>* ### nome [Lista]
>>* ### caminho [Lista]
>>* ### nomepasta [Lista]
>>* ### contato 'STRING'
>>* ### pastaCriada 'STRING'
>>
>>## **Funções** 
>>* ### Primeiro_passo
>>  * Verifico se na pasta de imagens tem imagens, se tiver pego o nome da imagens vou no google planilhas descobro o nome real da imagem,
criu uma pasta com esse nome e recorto a imagem para dentro dessa pasta com mais duas imagens essenciais.
>>
>>* ### Segundo_passo
>>  * Depois que eu adicionar alguns arquivos na pasta (tem que ser manual), com ela pronta esse passo vai zipar as pastas e salvar em outro diretorio 
e enviar por whatsapp para uma outra pessoa poder tratar as imagens.
>>* ### Terseiro_passo
>>  * Depois que as imagens estiver prontas eu vou receber as oastas zipadas por whatsapp, vou salvar em uma pasta especifica
e esse passo vai procurar a pasta com o mesmo nome vai envair o arquivos zipado para dentro 
e descompactar o arquivo dentro dessa pasta.
>>--- 
>>## __Bibliotecas__
>>~~~ Python
>>import os
>>import zipfile
>>from dataclasses import dataclass
>>from tkinter.filedialog import askdirectory
>>import shutil
>>from zipfile import ZipFile
>>import pandas as pd
>>import gspread
>>from os.path import basename
>>from funcoes import EnviaWhatsapp
>>import contatos
>>~~~
>---
>>## **agenda.db**
> > ### descrição
> > * Em andamento
> > ### Campos
> > * Nome
> > * telefone
> ---
> > ## funções
> > ### def Arquivos
> > * Em andamento
> >### def EnviaWhatsapp
> > * Em andamento
>>---
>>## __Bibliotecas__
>>~~~ Python 
>>from selenium import webdriver                                             
>>from selenium.webdriver.common.by import By
>>import time                                                                 
>>import os 
>---
> >## contatos
> >### def criarBanco
> > * Em andamento
> >### InserirDados
> > * Em andamento
> >### ExcluirNome
> > * Em andamento
> >### LerDados
> > * Em andamento
> >### BascarNome
> > * Em andamento
>>## __Bibliotecas__
>>~~~ Python 
>>import sqlite3, os
>>from contextlib import closing
> 
