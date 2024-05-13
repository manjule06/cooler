from tabulate import tabulate


class Process:
    def __init__(self, processID, arrivalTime, priority, burstTime):
        self.processID = processID
        self.arrivalTime = arrivalTime
        self.priority = priority
        self.burstTime = burstTime
        self.tempburstTime = burstTime
        self.responsetime = -1
        self.outtime = 0
        self.intime = -1
        self.turnaroundTime = 0  # New attribute to store turnaround time

def insert(Heap, value, heapsize, currentTime):
    start = heapsize[0]
    Heap[start] = value
    if Heap[start].intime == -1:
        Heap[start].intime = currentTime
    heapsize[0] += 1

    while start != 0 and Heap[(start - 1) // 2].priority > Heap[start].priority:
        Heap[(start - 1) // 2], Heap[start] = Heap[start], Heap[(start - 1) // 2]
        start = (start - 1) // 2

def order(Heap, heapsize, start):
    smallest = start
    left = 2 * start + 1
    right = 2 * start + 2
    if left < heapsize[0] and Heap[left].priority < Heap[smallest].priority:
        smallest = left
    if right < heapsize[0] and Heap[right].priority < Heap[smallest].priority:
        smallest = right

    if smallest != start:
        Heap[start], Heap[smallest] = Heap[smallest], Heap[start]
        order(Heap, heapsize, smallest)

def extractminimum(Heap, heapsize, currentTime):
    min_process = Heap[0]
    if min_process.responsetime == -1:
        min_process.responsetime = currentTime - min_process.arrivalTime
    heapsize[0] -= 1
    if heapsize[0] >= 1:
        Heap[0] = Heap[heapsize[0]]
        order(Heap, heapsize, 0)
    return min_process

def scheduling(Heap, array, n, heapsize, currentTime):
    if heapsize[0] == 0:
        return

    min_process = extractminimum(Heap, heapsize, currentTime)
    min_process.outtime = currentTime + 1
    min_process.burstTime -= 1  

    if min_process.burstTime > 0:
        insert(Heap, min_process, heapsize, currentTime)
        return

    for i in range(n):
        if array[i].processID == min_process.processID:
            array[i] = min_process
            break
        
def schedule_priority(array, n):
    array.sort(key=lambda x: x.arrivalTime)  # Sort by arrival time

    total_waiting_time = 0
    total_burst_time = 0
    total_turnaround_time = 0
    inserted_process = 0
    heap_size = [0]
    current_time = array[0].arrivalTime  
    total_response_time = 0

    Heap = [None] * (4 * n)

    for i in range(n):
        total_burst_time += array[i].burstTime
        array[i].tempburstTime = array[i].burstTime

    # Inserting the processes into Heap according to arrival time
    while True:
        if inserted_process != n:
            for i in range(n):
                if array[i].arrivalTime == current_time:
                    inserted_process += 1
                    array[i].intime = -1
                    array[i].responsetime = -1
                    insert(Heap, array[i], heap_size, current_time)
        scheduling(Heap, array, n, heap_size, current_time)
        current_time += 1
        if heap_size[0] == 0 and inserted_process == n:
            break

    for i in range(n):
        total_response_time += array[i].responsetime
        total_waiting_time += (array[i].outtime - array[i].intime - array[i].tempburstTime)
        total_turnaround_time += (array[i].outtime - array[i].intime)
        array[i].turnaroundTime = array[i].outtime - array[i].arrivalTime  # Calculate turnaround time for each process

    process_data = [(p.processID, p.arrivalTime, p.priority, p.tempburstTime, p.turnaroundTime) for p in array]  

    avg_waiting_time = total_waiting_time / n
    avg_response_time = total_response_time / n
    avg_turnaround_time = total_turnaround_time / n

    print(tabulate(process_data, headers=["Process ID", "Arrival Time", "Priority", "Burst Time", "Turnaround Time"], tablefmt="grid"))
    print(f"Average waiting time = {avg_waiting_time}")
    print(f"Average response time = {avg_response_time}")
    print(f"Average turn around time = {avg_turnaround_time}")

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    a = []
    for i in range(n):
        print(f"Process {i+1}:")
        processID = i + 1
        arrivalTime = int(input("Arrival Time: "))
        priority = int(input("Priority: "))
        burstTime = int(input("Burst Time: "))
        a.append(Process(processID, arrivalTime, priority, burstTime))
    schedule_priority(a, n)
