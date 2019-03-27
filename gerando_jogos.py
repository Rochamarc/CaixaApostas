from gera_bilhete import confere_bilhete,gera_premio
from datetime import datetime
from database_salvando import insere_jogos_feitos, insere_jogos_ganhos, insere_ganhadores

sorteio = gera_premio(20)
print("")
print(sorteio)
print("")
seguir = input("Tecle enter para continuar:")
arquivo_txt = ("docs/%s.txt" %(datetime.now()))
document = open(arquivo_txt,'w')

n_sorteio = 1

for i in range(1000000000):
    
    print("")
    jogo = ("JOGO NUMERO: %i" %i)
    print(jogo)
    print("")
    bilhete = gera_premio(50)
    acertos_feitos = confere_bilhete(sorteio,bilhete)
    print(acertos_feitos)
    insere_jogos_feitos(n_sorteio,str(bilhete))
    if acertos_feitos >= 15 or acertos_feitos == 0:
        insere_jogos_ganhos(n_sorteio,str(bilhete),str(sorteio),acertos_feitos)
        document.write('\n')
        document.write(jogo)
        document.write('\nSorteio\n')
        document.write(str(sorteio))
        document.write('\nBilhete:\n')
        document.write(str(bilhete))
        document.write('\nAcertos:\n')
        document.write(str(acertos_feitos))
        document.write('\n')

document.close()
