from database_funcoes import seleciona_n_jogadores,close_database,insere_premio
from random import randint
from gera_bilhete import gera_premio

#Determina o valor dos premios
def determina_premio():
    
    n_sorteio = int(input("Digite o valor do sorteio: "))
    #valor de acumulo a ser testado
    premio_acumulado = randint(500,2500000)
    try:
        jogadores = seleciona_n_jogadores(n_sorteio)
    except:
        print("O valor do sorteio não existe.")
        exit()
    
    valor_devolvido = (jogadores * 1.50) * 0.46 + premio_acumulado 
    valor_total_premio = 0

    #Calcula o valor dos premios e insere no banco de dados
    valor_total_insere = valor_devolvido
    valor_20 = valor_devolvido * 0.28
    valor_devolvido -= valor_20
    valor_0 = valor_devolvido * 0.18
    valor_devolvido -= valor_0
    valor_19 = valor_devolvido * 0.16
    valor_devolvido -= valor_19
    valor_18 = valor_devolvido * 0.16
    valor_devolvido -= valor_18
    valor_17 = valor_devolvido * 0.7
    valor_devolvido -= valor_17
    valor_16 = valor_devolvido * 0.7
    valor_devolvido -= valor_16
    valor_15 = valor_devolvido
    #inserindo valores no banco de dados
    insere_premio(n_sorteio,valor_total_insere,valor_20,valor_19,valor_18,valor_17,valor_16,valor_15,valor_0)

def confere_jogos():
    """ Conferir quais jogos foram ganhos e inserir na tabela de ganhadores """
    pass

determina_premio()
close_database()
