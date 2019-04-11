from random import choice

class GeradorDeBilhetes:
    def __init__(self,length):
        #defines 20 numbers  - prize, 50 numbers - gambles
        self.length = length

    def gera_bilhete(self):
        #creates a lista with 100 numbers
        self.bilhete = list(range(100))
        self.bilhete_premiado = []
        for i in range(self.length):
            numero = choice(self.bilhete)
            self.bilhete_premiado.append(numero)
            self.bilhete.remove(numero)
        self.bilhete_premiado.sort()
        return self.bilhete_premiado

class ConferirBilhetes:
    def __init__(self,bilhete_premiado,bilhete_jogado):
        self.bilhete_premiado = bilhete_premiado
        self.bilhete_jogado = bilhete_jogado
        
    def retorna_acertos(self):
        __acertos = 0
        for i in self.bilhete_premiado:
            if i in self.bilhete_jogado:
                __acertos += 1
        return __acertos


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

#TESTE DE FUNÇÔES
if __name__ == "__main__":
    bilhete = GeradorDeBilhetes(20)
    bilhete = bilhete.gera_bilhete()
    bilhete_2 = GeradorDeBilhetes(50)
    bilhete_2 = bilhete_2.gera_bilhete()
    confere_jogo = ConferirBilhetes(bilhete,bilhete_2)
    print(confere_jogo.retorna_acertos())