from gera_bilhete import GeradorDeBilhetes,ConferirBilhetes
import time

start = time.time()
bilhete = GeradorDeBilhetes(20).gera_bilhete()

for i in range(1000000):
    print(f'Rodada :{i}')
    apostador = GeradorDeBilhetes(50).gera_bilhete()
    acertos = ConferirBilhetes(bilhete,apostador).retorna_acertos()
    print(f'A rodada {i} teve {acertos}.')

end = time.time()
print(f'{end - start}ms para executar!')
