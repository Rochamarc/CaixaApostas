import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute("DELETE FROM bilhete_premiado")
c.execute("DELETE FROM ganhadores")
c.execute("DELETE FROM jogos_feitos")
c.execute("DELETE FROM jogos_ganhos")
c.execute("DELETE FROM premios_valor")

conn.commit()
c.close()