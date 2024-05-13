from tabulate import tabulate


def findWaitingTime(n, burst_time, wt, quantum):
    rem_bt = [0] * n
    for i in range(n):
        rem_bt[i] = burst_time[i]

    t = 0  

    while True:
        done = True
        for i in range(n):

            if rem_bt[i] > 0:
                done = False

                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - burst_time[i]
                    rem_bt[i] = 0
        if done:
            break

def findTurnAroundTime(n, burst_time, wt, tat):
    for i in range(n):
        tat[i] = burst_time[i] + wt[i]

def findavgTime(n, burst_time, quantum):
    wt = [0] * n
    tat = [0] * n
    findWaitingTime(n, burst_time, wt, quantum)
    findTurnAroundTime(n, burst_time, wt, tat)

    table_data = [["Processes", "Burst Time", "Waiting Time", "Turn-Around Time"]]
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        table_data.append([i + 1, burst_time[i], wt[i], tat[i]])

    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
    print("\nAverage waiting time = %.5f " % (total_wt / n))
    print("Average turn around time = %.5f " % (total_tat / n))

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))

    proc = []
    burst_time = []

    for i in range(n):
        proc_id = int(input(f"Enter process ID for process {i + 1}: "))
        proc.append(proc_id)
        burst = int(input(f"Enter burst time for process {proc_id}: "))
        burst_time.append(burst)

    quantum = int(input("Enter time quantum: "))

    findavgTime(n, burst_time, quantum)
