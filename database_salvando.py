import sqlite3
from datetime import datetime

conn = sqlite3.connect('data.db')
c = conn.cursor()
data_atual = datetime.now()

def insere_jogos_feitos(n_sorteio,bilhete,data=data_atual):
	global c
	global conn
	dados = [(n_sorteio,bilhete,data),]
	c.executemany("INSERT INTO jogos_feitos VALUES (?,?,?)",dados)
	print("Dados inseridos em jogos_feitos com sucesso!")
	conn.commit()

def insere_jogos_ganhos(n_sorteio,bilhete,bilhete_premiado,pontos):
	global c
	global conn
	dados = [(n_sorteio,bilhete,bilhete_premiado,pontos),]
	c.executemany("INSERT INTO jogos_ganhos VALUES (?,?,?,?)",dados)
	print("Dados inseridos em jogos_ganhos com sucesso!")
	conn.commit()

def insere_ganhadores(n_sorteio,pontos,bilhete,bilhete_premiado):
	global c
	global conn
	dados = [(n_sorteio,pontos,bilhete,bilhete_premiado),]
	c.executemany("INSERT INTO ganhadores VALUES (?,?,?,?)",dados)
	print("Dados inseridos ganhadores com sucesso!")
	conn.commit()
