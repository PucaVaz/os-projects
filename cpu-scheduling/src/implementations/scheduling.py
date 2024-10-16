"""
The scheduling algorithms to be
implemented are as follows:
- First-Come, First-Served (FCFS)
- Shortest Job First (SJF)
- Round Robin (RR)
"""
class Scheduling:
    def scheduling_fcfs(self, processes):
        """
        Implementation of the FCFS scheduling algorithm
        "First Come, First Served"
        The FCFS algorithm is a simple scheduling algorithm that schedules according to the arrival times of the processes.
        Processes are executed in the order they arrive.

        Input: list of dictionaries of processes in the format {"arrival": arrival, "burst": duration}
        Output: average turnaround time, average response time, average waiting time
        """

        n = len(processes)
        waiting_time = [0] * n
        turnaround_time = [0] * n
        response_time = [0] * n

        # Sort processes by arrival order, if they have the same arrival time, sort by execution order
        processes = sorted(processes, key=lambda x: x["arrival"])

        current_time = 0
        
        for i in range(n):
            # If the current time is less than the arrival time of the process, update the current time
            if current_time < processes[i]["arrival"]:
                current_time = processes[i]["arrival"]
            
            # Calculate response time, which is the time the process takes to start executing
            response_time[i] = current_time - processes[i]["arrival"]
            waiting_time[i] = response_time[i]
            
            # Update the current time
            current_time += processes[i]["burst"]
            
            # Calculate turnaround time, which is the time the process takes to be completed
            turnaround_time[i] = current_time - processes[i]["arrival"]

        average_turnaround_time = sum(turnaround_time) / n
        average_response_time = sum(response_time) / n
        average_waiting_time = sum(waiting_time) / n

        return average_turnaround_time, average_response_time, average_waiting_time

    def scheduling_sjf(self, processes):
        """
        Implementation of the SJF scheduling algorithm (Shortest Job First)
        The SJF algorithm is a scheduling algorithm that assigns the process with the shortest burst time first.

        Input: list of dictionaries of processes in the format {"arrival": arrival, "burst": duration}
        Output: average turnaround time, average response time, average waiting time
        """
        processes = sorted(processes, key=lambda x: x["arrival"])  # Sort processes by arrival order
        n = len(processes)
        waiting_time = [0] * n
        turnaround_time = [0] * n
        response_time = [0] * n
        
        time = 0
        waiting_queue = []
        done = 0
        
        while done < n:
            # Add processes that arrived by the current time to the waiting queue
            while processes and processes[0]["arrival"] <= time:
                waiting_queue.append(processes.pop(0))
            
            if waiting_queue:
                # Sort the waiting queue by burst time
                waiting_queue.sort(key=lambda x: x["burst"])
                
                # Process the shortest job
                current_process = waiting_queue.pop(0)
                index = n - len(processes) - len(waiting_queue) - 1
                
                if response_time[index] == 0:
                    response_time[index] = time - current_process["arrival"]
                
                time += current_process["burst"]
                turnaround_time[index] = time - current_process["arrival"]
                waiting_time[index] = turnaround_time[index] - current_process["burst"]
                
                done += 1
            else:
                # If the waiting queue is empty, advance time to the next process arrival
                time = processes[0]["arrival"]
        
        average_turnaround_time = sum(turnaround_time) / n
        average_response_time = sum(response_time) / n
        average_waiting_time = sum(waiting_time) / n
        
        return average_turnaround_time, average_response_time, average_waiting_time

    def scheduling_rr(self, processes, time_quantum=2):
        """
        Implementation of the RR scheduling algorithm (Round Robin)
        The RR algorithm is a scheduling algorithm that assigns a time quantum for each process.

        Input: list of dictionaries of processes in the format {"arrival": arrival, "burst": duration}
        Output: average turnaround time, average response time, average waiting time
        """
        n = len(processes)
        remaining_time = [p['burst'] for p in processes]
        completion_time = [0] * n
        turnaround_time = [0] * n
        waiting_time = [0] * n
        response_time = [-1] * n
        
        time = 0
        queue = []
        i = 0
        
        while True:
            # Add processes that arrived by the current time to the queue
            while i < n and processes[i]['arrival'] <= time:
                queue.append(i)
                i += 1
            # If the queue is empty, advance time to the next process arrival
            if not queue:
                if i >= n:
                    break
                time = processes[i]['arrival']
                continue
            
            current = queue.pop(0)
            # Calculate the response time of the process
            if response_time[current] == -1:
                response_time[current] = time - processes[current]['arrival']
            
            # Process the current process, if the remaining time is less than the quantum, process the remaining time
            if remaining_time[current] <= time_quantum:
                time += remaining_time[current]
                completion_time[current] = time
                remaining_time[current] = 0
            else:
                # Process the time quantum and add the process back to the queue
                time += time_quantum
                remaining_time[current] -= time_quantum
                
                # Add processes that arrived by the current time to the queue
                while i < n and processes[i]['arrival'] <= time:
                    queue.append(i)
                    i += 1
                
                queue.append(current)
        
        # Calculate the turnaround time and waiting time of each process
        for i in range(n):
            turnaround_time[i] = completion_time[i] - processes[i]['arrival']
            waiting_time[i] = turnaround_time[i] - processes[i]['burst']
        
        average_turnaround_time = sum(turnaround_time) / n
        average_response_time = sum(response_time) / n
        average_waiting_time = sum(waiting_time) / n
        
        return average_turnaround_time, average_response_time, average_waiting_time
