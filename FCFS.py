from tabulate import tabulate


def CalculateWaitingTime(at, bt, N):
    wt = [0] * N
    tat = [0] * N  # Turnaround time
    wt[0] = 0
    tat[0] = bt[0]  # First process's turnaround time is its burst time

    table_data = []
    table_data.append(["P.No.", "Arrival Time", "Burst Time", "Waiting Time", "Turnaround Time"])
    table_data.append(["1", at[0], bt[0], wt[0], tat[0]])

    for i in range(1, N):
        wt[i] = (at[i - 1] + bt[i - 1] + wt[i - 1]) - at[i]
        tat[i] = bt[i] + wt[i]  # Turnaround time calculation
        table_data.append([i + 1, at[i], bt[i], wt[i], tat[i]])

    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

    average_wt = sum(wt) / N
    average_tat = sum(tat) / N

    print("Average waiting time =", average_wt)
    print("Average turnaround time =", average_tat)


if __name__ == '__main__':
    N = 5

    at = [0, 1, 2, 3, 4]
    bt = [4, 3, 1, 2, 5]

    CalculateWaitingTime(at, bt, N)
