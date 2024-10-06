from src.helper_functions import load_processes, print_results, simulate_page_replacement_algorithm
from src.algorithms import FIFOPageReplacement, OptimalPageReplacement, PageReplacementAlgorithm
import sys

def main():
    capacity, page_references = load_processes(sys.argv[1])
    
    print_results("FIFO",simulate_page_replacement_algorithm(capacity, page_references, FIFOPageReplacement))
    print_results("OTM",simulate_page_replacement_algorithm(capacity, page_references, OptimalPageReplacement))
if __name__ == "__main__":
    main()