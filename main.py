from database_funcoes import *
from random import randint
from gera_bilhete import GeradorDeBilhetes,ConferirBilhetes
import json 
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

    #Calcula o valor dos premios
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
    sorteio = GeradorDeBilhetes(20).gera_bilhete()
    insere_sorteio(n_sorteio,str(sorteio))
    print("Sorteio executado com sucesso!")

def organizando_ganhadores(n_sorteio):
    """ 
            Duas seleções nos banco de dados, 
    Primeira seleção - bilhete_premiado --> bilhete = list(bilhete)
    Segunda seleção - jogos_feitos --> bilhete = list(bilhete)
    Sera criado uma cadeia de if para gerar os ganhos e
    serão inseridos no banco de dados jogos_ganhos os ganhadores
    """
    bilhete_premiado = retorna_bilhete_premiado(n_sorteio)
    bilhetes_jogados = retorna_bilhetes_jogados(n_sorteio)
    cont = 0 #teste
    for i in bilhetes_jogados:
        cont += 1 #teste
        bilhete = json.loads(i[0])
        acertos = ConferirBilhetes(bilhete_premiado,i).retorna_acertos()
        if acertos >= 15 or acertos == 0:
            #funcionando
            insere_jogos_ganhos(n_sorteio,str(bilhete),str(bilhete_premiado),acertos)
        
        
def confere_jogos(n_sorteio):
    """
    Seleciona no banco de dados jogos_ganhos, e os organize em dos ganhadores do 15 ao 0
    depois obtenha os valores de cada ramo ganhado e divida entre os ganhadores 
    e salve no banco de dados ganhadores com seus respectivos premios
    caso algum ramo não possua ganhador, o valor e será acumulado para o proximo jogo
    """
    ganhadores = retorna_dicionario_ganhadores(n_sorteio)
    
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
                                [ 5 ] - Organizar os vencedores
                                [ 6 ] - Sair
    """)
    opcao = int(input("                             --->. "))
    if opcao == 1:
        n_sorteio = int(input("                         Digite o número do sorteio: "))
        contagem_jogos_feitos(n_sorteio)
    elif opcao == 4:
        n_sorteio = int(input("                         Digite o número do sorteio: "))
        determina_premio(n_sorteio)
    elif opcao == 5:
        n_sorteio = int(input("                         Digite o número do sorteio: "))
        organizando_ganhadores(n_sorteio)
    elif opcao == 6:
        print("Fechando banco de dados...")
        close_database()
        print("Até a próxima!!!")
        exit()

