"""
Auxiliary functions for the process scheduler
"""

def print_results(algorithm, results):
    """
    Prints the results of the scheduling algorithms

    Input: algorithm, dictionary of results in the format {"turnaround": avg_turnaround, "response": avg_response, "wait": avg_wait}
    Output: None
    """
    print(f"{algorithm} {results[0]:.1f}".replace('.', ',') + f" {results[1]:.1f}".replace('.', ',') + f" {results[2]:.1f}".replace('.', ','))

def load_processes(file_path):
    """
    Loads the processes from the input file into a dictionary
    
    Input: path to the input file
    Output: list of dictionaries of processes in the format {"arrival": arrival, "burst": duration}
    """
    processes = []
    try:
        # Read the input file provided as an argument
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip():
                    break
                arrival, duration = map(int, line.split())
                # Add the process to the dictionary
                processes.append({"arrival": arrival, "burst": duration})
    except FileNotFoundError:
        print("File not found")
    return processes
