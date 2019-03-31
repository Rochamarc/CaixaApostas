from random import choice

def gera_bilhete():
    bilhete = []
    for i in range(100):
        bilhete.append(i)
    return bilhete

def gera_premio(extension):
    valor_lista = gera_bilhete()
    sorteio = []
    for i in range(extension):
        valor = choice(valor_lista)
        sorteio.append(valor)
        valor_lista.remove(valor)
        #ordena a lista
        sorteio.sort()
    return sorteio

def confere_bilhete(bilhete_sorteado,bilhete):
    acertos = 0
    for i in bilhete_sorteado:
        if i in bilhete:
            acertos += 1
    return acertos

if __name__ == "__main__":
    #testa as funçoes
    sorteio = gera_premio(20)
    print(sorteio)
    jogador = gera_premio(50)
    print(jogador)
    confere_bilhete(sorteio,jogador)