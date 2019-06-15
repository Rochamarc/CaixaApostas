from gera_bilhete import GeradorDeBilhetes
from datetime import datetime
from database_funcoes import insere_jogos_feitos, insere_jogos_ganhos, insere_ganhadores, insere_premio,close_database
from random import randint

#define o numero do sorteio
n_sorteio = int(input("Digite o numero do sorteio: "))
#numero aleatorio de apostadores
apostadores = randint(500,10000)

for i in range(apostadores):
    
    print("")
    print(f"JOGO NUMERO: {i}")
    print("")
    bilhete = GeradorDeBilhetes(50).gera_bilhete()
    insere_jogos_feitos(n_sorteio,str(bilhete))

close_database()