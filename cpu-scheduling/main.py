"""
Main file that will read the input file and apply the scheduling algorithms: FCFS, SJF, and RR.
It will print the results in the following order: avg_turnaround, avg_response, and avg_wait.
An example of the input file is:
0 20
0 10
4 6
4 8
And an example of the output is:
FCFS 30.5 19.5 19.5
SJF 21.5 10.5 10.5
RR 31.5 2.0 20.5
"""

import sys

# Local libraries
from src.implementations import Scheduling
from src.helpers import print_results, load_processes

def main():
    if len(sys.argv) > 1:
        processes = load_processes(sys.argv[1])
    else:
        processes = load_processes("input.txt")

    # Apply the scheduling algorithms
    scheduling_algorithms = Scheduling()
    
    # Calculate the results of the scheduling algorithms
    fcfs = scheduling_algorithms.scheduling_fcfs(processes)
    sjf = scheduling_algorithms.scheduling_sjf(processes)
    rr = scheduling_algorithms.scheduling_rr(processes)

    # Print the results of the scheduling algorithms in the order avg_turnaround, avg_response, and avg_wait
    print_results("FCFS", fcfs)
    print_results("SJF", sjf)
    print_results("RR", rr)

if __name__ == "__main__":
    main()
