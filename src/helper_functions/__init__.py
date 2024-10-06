"""
This module contains helper functions for the page replacement algorithms.
"""
def print_results(algorithm, page_faults):
    """
    Loads processes from a specified file. If no file is provided, defaults to 'input.txt'.
    
    Args:
        algorithm (str): The name of the algorithm.
        page_faults (int): The number of page faults.
    
    Returns:
        None
    """
    print(f"{algorithm} {page_faults}")

def load_processes(file_path=None):
    """
    Loads processes from a specified file. If no file is provided, defaults to 'input.txt'.
    
    Args:
        file_path (str): The path to the input file. If None, uses 'input.txt'.
        
    Returns:
        tuple: A tuple containing the capacity (int) and a list of page references (list of int).
    """
    capacity = 0
    page_references = []

    if file_path is None:
        file_path = "input.txt"

    try:
        with open(file_path, 'r') as file:
            capacity = int(file.readline().strip())
            page_references = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None
    except ValueError:
        print("Erro ao converter valores do arquivo")
        return None
    
    return capacity, page_references


def simulate_page_replacement_algorithm(capacity, page_references, algorithm_class):
    # Check if the algorithm class has a page_references, only used in Optimal
    if 'page_references' in algorithm_class.__init__.__code__.co_varnames:
        algorithm_instance = algorithm_class(capacity=capacity, page_references=page_references)
    else:
        algorithm_instance = algorithm_class(capacity=capacity)

    for page_number in page_references:
        algorithm_instance.insert_page(page_number)
    
    total_page_faults = algorithm_instance.get_page_faults()
    return total_page_faults

