import sqlite3
from datetime import datetime
from tabulate import tabulate

conn = sqlite3.connect('data.db')
c = conn.cursor()
data_atual = datetime.now()

""" Funções de inserção no banco de dados """
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

def insere_sorteio(n_sorteio,sorteio,connector=conn,cursor=c):
	cursor.execute("SELECT valor_total_premio FROM premios_valor WHERE n_sorteio=?",(n_sorteio,))
	valor_premio = cursor.fetchall()[-1]
	for i in valor_premio:
		dados = [(n_sorteio,sorteio,i),]
	cursor.executemany("INSERT INTO bilhete_premiado VALUES (?,?,?)",dados)
	print("Dados inseridos em bilhete_premiado com sucesso!")
	connector.commit()

def devolve_acumulo():
	return aculumo

""" Funções de leitura do banco de dados """
def seleciona_ganhadores(n_sorteio,cursor=c):
	#seleciona os ganhadores da tabela numero sorteio
	cursor.execute(" SELECT * FROM jogos_ganhos WHERE n_sorteio=?; ",(n_sorteio,))
	data = []
	headers = ['Sorteio','Bilhete','Pontos']
	for tabela in cursor.fetchall():
    		data.append(tabela)
	print(tabulate(data,headers))

""" Funções de leitura e retorno """
#Seleciona a tabela jogos_feitos e determina o numero de jogadores 
def seleciona_n_jogadores(n_sorteio,cursor=c):
	cursor.execute("SELECT * FROM jogos_feitos WHERE n_sorteio=?",(n_sorteio,))
	cont = 0
	for tabela in cursor.fetchall():
		cont += 1
	print("%i jogos feitos." %(cont))
	return cont

def retorna_jogadores(n_sorteio,cursor=c):
	cursor.execute("SELECT * FROM jogos_feitos WHERE n_sorteio=?",(n_sorteio,))
	return cursor.fetchall()

""" Função de fechamento do banco de dados """
def close_database(connector=conn):
	connector.close()

#Teste, só funcionam quando este codigo for diretamente executado
if __name__ == "__main__":
	pass