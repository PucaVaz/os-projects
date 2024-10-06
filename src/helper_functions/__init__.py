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
    """
    capacity = 0
    page_references = []
    try:
        # Ler o arquivo de entrada passado como argumento
        if not file_path:
            file_path =  "input.txt"
        with open(file_path, 'r') as file:
            capacity = int(file.readline().strip())
            page_references= [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except ValueError:
        print("Erro ao converter valores do arquivo")
        return None
    return capacity, page_references

def simulate_page_replacement_algorithm(capacity, page_references, algorithm_class):
    algorithm_instance = algorithm_class(capacity=capacity, page_references=page_references)
    for page_number in page_references:
        algorithm_instance.insert_page(page_number)
    total_page_faults = algorithm_instance.get_page_faults()
    return total_page_faults
