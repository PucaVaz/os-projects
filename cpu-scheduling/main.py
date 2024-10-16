"""
Arquivo principal que irá ler o arquivo de entrada e aplicar os algoritmos de escalonamento, o FCFS, SJF e RR.
e imprimir na seguinte ordem avg_turnaround, avg_response e avg_wait.
Um exemplo do arquivo de entrada é:
0 20
0 10
4 6
4 8
e um exemplo da saída é:
FCFS 30,5 19,5 19,5
SJF 21,5 10,5 10,5
RR 31,5 2,0 20,5
"""
import sys

# Bibliotecas locais
from src.implementacoes import Escalonamento
from src.misc import print_results, load_processes

def main():
    # Carregar os processos do arquivo de entrada em um diciário
    processos = load_processes(sys.argv[1])

    # Aplica os algoritmos de escalonamento
    algoritmos_de_escalonamento = Escalonamento()
    
    # Calcula os resultados dos algoritmos de escalonamento
    fcfs = algoritmos_de_escalonamento.escalonamento_fcfs(processos)
    sjf = algoritmos_de_escalonamento.escalonamento_sjf(processos)
    rr = algoritmos_de_escalonamento.escalonamento_rr(processos)

    # Imprime os resultados dos algoritmos de escalonamento na ordem avg_turnaround, avg_response e avg_wait
    print_results("FCFS", fcfs)
    print_results("SJF", sjf)
    print_results("RR", rr)

if __name__ == "__main__":
    main()
