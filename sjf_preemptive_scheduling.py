def sjf_preemptive_scheduling(at, bt, N):
    processes = []
    for i in range(N):
        processes.append((i+1, at[i], bt[i]))
    processes.sort(key=lambda x: x[1])

    wt = [0]*N
    tat = [0]*N
    ft = [0]*N
    remaining_bt = bt[:]
    total_bt = sum(bt)
    time = 0

    while time < total_bt:
        min_bt = float('inf')
        next_process = -1
        for i in range(N):
            if at[i] <= time and remaining_bt[i] < min_bt and remaining_bt[i] > 0:
                min_bt = remaining_bt[i]
                next_process = i
        if next_process == -1:
            time += 1
            continue
        remaining_bt[next_process] -= 1
        time += 1
        if remaining_bt[next_process] == 0:
            wt[next_process] = time - at[next_process] - bt[next_process]
            tat[next_process] = wt[next_process] + bt[next_process]
            ft[next_process] = time

    total_wt = sum(wt)
    total_tat = sum(tat)
    total_ft = sum(ft)
    average_wt = total_wt / N
    average_tat = total_tat / N
    average_ft = total_ft / N

    print("P.No.\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tFinish Time")
    for i in range(N):
        print(processes[i][0], "\t\t", processes[i][1], "\t\t", processes[i][2], "\t\t", wt[i], "\t\t", tat[i], "\t\t", ft[i])
    print("Average waiting time =", average_wt)
    print("Average turnaround time =", average_tat)
    print("Average finish time =", average_ft)

if __name__ == '__main__':
    N = 5
    at = [0, 1, 2, 3, 4]  # arrival time
    bt = [4, 3, 1, 2, 5]  # burst time

    print("\nSJF Scheduling (Preemptive):")
    sjf_preemptive_scheduling(at, bt, N)
