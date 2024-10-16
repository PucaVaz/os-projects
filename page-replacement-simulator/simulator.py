from src.helper_functions import load_processes, print_results, simulate_page_replacement_algorithm
from src.algorithms import FIFOPageReplacement, OptimalPageReplacement, LeastUsedPageReplacement
import sys

def main():
    if len(sys.argv) > 1:
        capacity, page_references = load_processes(sys.argv[1])
    else:
        capacity, page_references = load_processes() 

    print_results("FIFO",simulate_page_replacement_algorithm(capacity, page_references, FIFOPageReplacement))
    print_results("OTM",simulate_page_replacement_algorithm(capacity, page_references, OptimalPageReplacement))
    print_results("LRU",simulate_page_replacement_algorithm(capacity, page_references, LeastUsedPageReplacement))

if __name__ == "__main__":
    main()