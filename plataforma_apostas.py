from random import randint

class Apostador:

    __bilhete_reverso = list(range(100))
    __bilhete_marcado = []

    def ver_bilhete(self):
        print("Este é o seu bilhete.")
        print(self.bilhete_marcado)
        print("Este é o seu bilhete reverso.")
        print(self.bilhete_reverso)
    #marca o bilhete
    def marcar_bilhete(self,*numeros):
        for i in numeros:
            self.__bilhete_marcado.append(i)
        
    #faz uma aposta espelho
    def aposta_reversa(self):
        for i in self.__bilhete_marcado:
            self.__bilhete_reverso.remove(i)
        
    #Marca os numeros restantes 
    def marcar_pelo_volante(self):
        while len(self.__bilhete_marcado) < 50:
            numero = randint(0,99)
            if not numero in self.__bilhete_marcado:
                self.__bilhete_marcado.append(numero)
    
    def retornar_bilhete_premiado(self):
        self.__bilhete_marcado.sort()
        return self.__bilhete_marcado

    def retornar_bilhete_reverso(self):
        self.__bilhete_reverso.sort()
        return self.__bilhete_reverso

#Funcoes teste
if __name__ == "__main__":
    #funciona
    apostador = Apostador()
    apostador.marcar_bilhete(0,1,2,5,6,3,7,9)
    apostador.marcar_pelo_volante()
    apostador.aposta_reversa()
    bilhete = apostador.retornar_bilhete_premiado()
    bilhete_reverso = apostador.retornar_bilhete_reverso()
    print(bilhete)
    print(bilhete_reverso)