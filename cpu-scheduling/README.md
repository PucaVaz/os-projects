# CPU Scheduling Algorithms

This Python program applies three scheduling algorithms—FCFS, SJF, and RR—to a set of processes and prints the average turnaround time, average response time, and average waiting time for each algorithm.

## Input Format

The input consists of a series of integer pairs separated by a space, indicating the arrival time and duration of each process. The input ends at the end of the file.

## Output Format

The output consists of lines containing the abbreviation of each of the three algorithms and the values of the three requested metrics.

Each line presents the algorithm abbreviation and the average values (with one decimal place) for turnaround time, response time, and waiting time, in exactly this order, separated by a space.

## How to Run

1. Move to this folder:
   ```bash
   cd cpu-scheduling
   ```

2. Run the code:
    ```bash
    python3 main.py 
    ```
    or specify the path that you will use
    ```bash
    python3 main.py input.txt
    ```

### Example Input File:
```bash
0 20
0 10
4 6
4 8
```

### Expected Output:
```bash
FCFS 30.5 19.5 19.5
SJF 21.5 10.5 10.5
RR 31.5 2.0 20.5
```