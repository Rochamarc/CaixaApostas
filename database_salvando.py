import sqlite3
from datetime import datetime

conn = sqlite3.connect('data.db')
c = conn.cursor()
data_atual = datetime.now()

def insere_jogos_feitos(n_sorteio,bilhete,data=data_atual,connector=conn,cursor=c):
	dados = [(n_sorteio,bilhete,data),]
	cursor.executemany("INSERT INTO jogos_feitos VALUES (?,?,?)",dados)
	print("Dados inseridos em jogos_feitos com sucesso!")
	connector.commit()

def insere_jogos_ganhos(n_sorteio,bilhete,bilhete_premiado,pontos,connector=conn,cursor=c):
	dados = [(n_sorteio,bilhete,bilhete_premiado,pontos),]
	cursor.executemany("INSERT INTO jogos_ganhos VALUES (?,?,?,?)",dados)
	print("Dados inseridos em jogos_ganhos com sucesso!")
	connector.commit()

def insere_ganhadores(n_sorteio,pontos,bilhete,bilhete_premiado,valor_premio,connector=conn,cursor=c):
	dados = [(n_sorteio,pontos,bilhete,bilhete_premiado,valor_premio),]
	cursor.executemany("INSERT INTO ganhadores VALUES (?,?,?,?,?)",dados)
	print("Dados inseridos em ganhadores com sucesso!")
	connector.commit()

def insere_premio(n_sorteio,valor_total_premio,valor_20,valor_19,valor_18,valor_17,valor_16,valor_15,valor_0,connector=conn,cursor=c):
	dados = [(n_sorteio,valor_total_premio,valor_20,valor_19,valor_18,valor_17,valor_16,valor_15,valor_0),]
	cursor.executemany("INSERT INTO premios_valor VALUES(?,?,?,?,?,?,?,?,?)",dados)
	print("Dados inseridos em premios com sucesso!")
	connector.commit()


def devolve_acumulo():
	return aculumo
