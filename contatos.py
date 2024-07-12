import sqlite3, os
from contextlib import closing

# Criei um banco de dados com uma tabela chamada contatos para salvar os contatos que vou enviar ps arquivos no whatsapp

def criarBanco():
    if 'agenda.db' in os.listdir('.'):
        print('Banco de dados já existe, tente inserir ou visualizar o banco')
    else:
        conecao = sqlite3.connect('agenda.db')
        cursor = conecao.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, telefone varchar)')

def InserirDados(nome,telefone):
    with sqlite3.connect('agenda.db') as conecao:
        with closing(conecao.cursor()) as curso:
            curso.execute('insert into cadastro (nome, telefone) values(?,?)',(nome,telefone))
            conecao.commit()
            print('Linhas afetadas',curso.rowcount)

def ExcluirNome(nome):
    with sqlite3.connect('agenda.db') as conecao:
        with closing(conecao.cursor()) as curso:
            curso.execute(F"delete from cadastro where nome = '{nome}'")
            print('Linhas afetadas',curso.rowcount)
            if curso.rowcount >= 1:
                conecao.commit()
            else:
                conecao.rollback()
                print(f'Nome {nome} não encontrado')
def LerDados():
    contatos=[]
    with sqlite3.connect('agenda.db') as conecao:
        with closing(conecao.cursor()) as curso:
            curso.execute('select * from cadastro')
            '''print(f'{"Nome":^20}|{"Telefone":^13}')
            print('=================================')'''
            while True:
                resultado = curso.fetchone()
                if resultado is None:
                    break
                #print(f'{resultado[0]:<20}|{resultado[1]:<13}')
                contatos.append(resultado)
    return contatos



def BascarNome(nome):
    with sqlite3.connect('agenda.db') as conecao:
        with closing(conecao.cursor()) as curso:
            curso.execute(F"select * from cadastro where nome = '{nome}'")
            print(f'{"Nome":^20}|{"Telefone":^13}')
            print('=================================')
            while True:
                resultado = curso.fetchone()
                if resultado is None:
                    break
                print(f'{resultado[0]:<20}|{resultado[1]:<13}')

def NumeroTell(nome):
    with sqlite3.connect('agenda.db') as conecao:
        with closing(conecao.cursor()) as curso:
            curso.execute(F"select * from cadastro where nome = '{nome}'")
            while True:
                resultado = curso.fetchone()
                if resultado is None:
                    break
                reslt = resultado[1]
    return reslt

if __name__=='__main__':
    #criarBanco()
    #InserirDados("Fernando","11945922382")
    #LerDados()
    #ExcluirNome('Fernando')
    print(NumeroTell('Renan'))