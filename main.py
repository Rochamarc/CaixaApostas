from database_funcoes import seleciona_n_jogadores,close_database,insere_premio,insere_sorteio
from random import randint
from gera_bilhete import gera_premio

#Determina o valor dos premios
def contagem_jogos_feitos(n_sorteio):
    
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

#Determina sorteio e o valor do premio
def determina_premio(n_sorteio):
    sorteio = gera_premio(20)
    insere_sorteio(n_sorteio,str(sorteio))
    print("Sorteio executado com sucesso!")

def confere_jogos(n_sorteio):
    pass

while True:
    print("""
                                ##################################
                                        CENTRAL DE APOSTAS
                                ##################################
                                     SE SENTINDO SORTUDO HOJE?


                                [ 1 ] - Contar o número de jogadores
                                [ 2 ] - Conferir os ganhadores
                                [ 3 ] - Visualizar o valor dos premios
                                [ 4 ] - Sortear os numeros ganhadores
    """)
    opcao = int(input("                             --->. "))
    if opcao == 1:
        n_sorteio = int(input("                         Digite o número do sorteio: "))
        contagem_jogos_feitos(n_sorteio)
    elif opcao == 4:
        n_sorteio = int(input("                         Digite o número do sorteio: "))
        determina_premio(n_sorteio)
    elif funcao == 5:
        print("Fechando banco de dados...")
        close_database()
        print("Até a próxima!!!")
        exit()

