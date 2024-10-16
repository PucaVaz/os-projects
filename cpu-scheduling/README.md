# Algoritmos de escalonamento de CPU

Este programa em Python aplica três algoritmos de escalonamento - FCFS, SJF e RR - a um conjunto de processos e imprime o tempo médio de retorno, o tempo médio de resposta e o tempo médio de espera para cada algoritmo.

## Formato de entrada

A entrada é composta por uma série de pares de
números inteiros separados por um espaço em branco
indicando o tempo de chegada e a duração de cada
processo. A entrada termina com o fim do arquivo.

## Formato de saída

A saída é composta por linhas contendo a sigla de
cada um dos três algoritmos e os valores das três
métricas solicitadas.

Cada linha apresenta a sigla do algoritmo e os
valores médios (com uma casa decimal) para tempo
de retorno, tempo de resposta e tempo de espera,
exatamente nesta ordem, separados por um espaço
em branco.
## Como executar

```bash
python3 main.py input.txt
```

### Exemplo de arquivo de entrada:
```bash
0 20
0 10
4 6
4 8
```

### Saída esperada:
``` bash
FCFS 30,5 19,5 19,5 
SJF 21,5 10,5 10,5
RR 31,5 2,0 20,5
```