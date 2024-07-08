import sqlite3, time, os
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
    with sqlite3.connect('agenda.db') as conecao:
        with closing(conecao.cursor()) as curso:
            curso.execute('select * from cadastro')
            print('Nome     |     Telefone')
            print('=======================')
            while True:
                resultado = curso.fetchone()
                if resultado is None:
                    break
                print(f'{resultado[0]}          {resultado[1]}')

def BascarNome(nome):
    with sqlite3.connect('agenda.db') as conecao:
        with closing(conecao.cursor()) as curso:
            curso.execute(F"select * from cadastro where nome = '{nome}'")
            while True:
                resultado = curso.fetchone()
                if resultado is None:
                    break
                print(f'{resultado[0]}          {resultado[1]}')



if __name__=='__main__':
    #criarBanco()
    #InserirDados("Fernando","11945922382")
    #LerDados()
    #ExcluirNome('Fernando')
    BascarNome('Fernando')