"""
 Funções auxiliares para o algoritmos de substituição de paginas
"""
def print_results(algorithm, page_faults):
    """
    Imprime os resultados dos algoritmos de escalonamento

    Entrada: Nome do algoritmo e falta de paginas
    Saída: None
    """
    print(f"{algorithm} {page_faults}")

def load_processes(file_path):
    """
    Carrega os processos do arquivo de entrada em um dicionário
    
    Entrada: caminho do arquivo de entrada
    Saída: Dicionário com a quantidade de quadros de memória e os processos
    """
    memory_simulation_data = {}
    try:
        # Ler o arquivo de entrada passado como argumento
        with open(file_path, 'r') as file:
            memory_simulation_data['frames'] = int(file.readline().strip())
            memory_simulation_data['processes'] = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except ValueError:
        print("Erro ao converter valores do arquivo")
        memory_simulation_data = {}
    return memory_simulation_data
