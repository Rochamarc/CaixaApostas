from gera_bilhete import confere_bilhete,gera_premio
from datetime import datetime
from database_salvando import insere_jogos_feitos, insere_jogos_ganhos, insere_ganhadores, insere_premio

sorteio = gera_premio(20)
print("")
print(sorteio)
print("")
seguir = input("Tecle enter para continuar:")
arquivo_txt = ("docs/%s.txt" %(datetime.now()))
document = open(arquivo_txt,'w')

n_sorteio = int(input("Digite o numero do sorteio: "))
valor_total_premio = 0
#valor de acumulo a ser testado
acumulo = 1500000.00

for i in range(100):
    
    valor_total_premio += 1.50
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

#Calcula o valor dos premios e insere no banco de dados
valor_devolvido = acumulo + (0.46 * valor_total_premio)
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
