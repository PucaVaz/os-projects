"""
 Funções auxiliares para o escalonador de processos
"""
def print_results(algorithm, results):
    """
    Imprime os resultados dos algoritmos de escalonamento

    Entrada: algoritmo, dicionario dos resultados no formato {"turnaround": avg_turnaround, "response": avg_response, "wait": avg_wait}
    Saída: None
    """
    print(f"{algorithm} {results[0]:.1f}".replace('.', ',') + f" {results[1]:.1f}".replace('.', ',') + f" {results[2]:.1f}".replace('.', ','))

def load_processes(file_path):
    """
    Carrega os processos do arquivo de entrada em um dicionário
    
    Entrada: caminho do arquivo de entrada
    Saída: lista de dicionários dos processos no formato {"chegada": arrival, "burst": duration}
    """
    processos = []
    try:
        # Ler o arquivo de entrada passado como argumento
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip():
                    break
                arrival, duration = map(int, line.split())
                # Adiciona o processo no dicionário
                processos.append({"chegada": arrival, "burst": duration})
    except FileNotFoundError:
        print("Arquivo não encontrado")
    return processos