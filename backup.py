import sqlite3 
from database_funcoes import seleciona_jogos_feitos
conn = sqlite3.connect('data_backup.db')
c = conn.cursor()

def jogos_feitos_backup(connector=conn,cursor=c):
    list_jogos_feitos = seleciona_jogos_feitos()
    for i in list_jogos_feitos:
        cursor.executemany("INSERT INTO jogos_feitos VALUES (?,?,?)",i)
        print("Backup jogos_feitos realizados com sucesso!")
    connector.commit()

def close_database(connector=conn):
    connector.close()

jogos_feitos_backup()