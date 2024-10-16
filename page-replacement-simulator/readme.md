# Page Replacement Algorithm Simulator

## Overview

This project simulates the functionality of three primary page replacement algorithms used in Operating Systems:

- **FIFO (First In, First Out)**
- **OTM (Optimal Replacement)**
- **LRU (Least Recently Used)**

The goal is to determine the number of page faults for each algorithm given a sequence of page references and a fixed number of frames in memory.

This project was developed as part of the **Operating Systems I** course at the **Federal University of Paraíba**.

## Features

- Simulates the behavior of the three page replacement algorithms.
- Reads input from a file and outputs the number of page faults for each algorithm.
- Precise output formatting as per the project requirements.

## Input and Output

### Input Format
- A series of integers where:
  - The first number represents the number of available frames in memory.
  - The subsequent numbers represent the sequence of page references.
  
### Example Input:
```
4
1
2
3
4
1
2
5
1
2
3
4
5
```

### Output Format
The program outputs the number of page faults for each algorithm in the following format:

```
FIFO <page_faults_FIFO>
OTM <page_faults_OTM>
LRU <page_faults_LRU>
```

### Example Output:
```
FIFO 10
OTM 6
LRU 8
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/pucavaz/page-replacement-simulator.git
   cd page-replacement-simulator
   ```

2. Compile or run the code:
   ```bash
   python simulator.py 
   ```
   or pass as an argument which file do you want to use
   ```bash
   python simulator.py input.txt
   ```
3. Ensure the input file follows the format described above. The output will display the number of page faults for each algorithm.

## Requirements

- Python 3.x 

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to modify the repository link and the programming language used based on your actual implementation!