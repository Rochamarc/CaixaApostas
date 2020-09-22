#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	// Variaveis para iniciar o tempo de execuçao
	clock_t start, end;
	double cpu_time_used;

	start = clock(); // Inicia o relogio
	//declarando variaveis
	int segundos = time(0);
	srand(segundos);
	int bilhete[20];
	int apostador[50];
	
	// Sorteio 
	//cria os valores dentro do array
	for (int i = 0; i < 20; i++){
		int numero_aleatorio = rand() %100;
		//printf("O numero aleatorio é: %d\n", numero_aleatorio);
		bilhete[i] = numero_aleatorio;		
	}
	
	//testa se tem valores iguais dentro do array
	//funcionando corretamente, retirado os prints de debug
	for(int y = 0; y < 20; y ++){
		int numero_aleatorio = rand() %100;
		//cria um ponteiro dentro do array
		for(int w = 0; w < 20; w++){
			int valor_testado = bilhete[y];
			if (valor_testado == bilhete[w]){
				if(y == w){
					continue;
				} else {
					bilhete[y] = numero_aleatorio;
				}
			}
		}
	}
	
	// Começa a criaçao dos jogos 
	for(int z = 0; z < 1000000; z++){
		int pontuacao = 0;
		//Declara as rodadas
		printf("Rodada: %d \n\n",z);
		
		// Aposta
		for(int i = 0; i < 50; i++){
			int numero_aleatorio = rand() %100;
			apostador[i] = numero_aleatorio;
		}

		for(int y = 0; y < 50; y++){
			int numero_aleatorio = rand() %100;
			for(int w = 0; w < 50; w++){
				int valor_testado = apostador[y];
				if(valor_testado == apostador[w]){
					if(y == w){
						continue;
					} else {
						apostador[y] = numero_aleatorio;
					}
				}
			}
		}
		
		// Testa os numeros da aposta com os numeros do sorteio
		for(int i = 0; i < 50; i++){
			int valor_apostador = apostador[i];
			for(int y = 0; y < 20; y++){
				int valor_aposta = bilhete[y];
				if(valor_apostador == valor_aposta){
					pontuacao++;
				}
			}
		}

		//finaliza a rodada
		printf("Rodada %d teve %d pontos...\n",z,pontuacao);
		printf("Finalizando rodada : %d\n",z);
	}

	end = clock(); // Finaliza o relgio
	cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	printf("%f Para a execucao do codigo!\n",cpu_time_used);
	
	return 0;
}
