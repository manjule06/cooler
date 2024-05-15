def main():
    processes = int(input("number of processes : "))
    resources = int(input("number of resources : "))
    max_resources = [int(i) for i in input("maximum resources : ").split()]

    print("\n-- allocated resources for each process --")
    currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    print("\n-- maximum resources for each process --")
    max_need = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    allocated = [0] * resources
    for i in range(processes):
        for j in range(resources):
            allocated[j] += currently_allocated[i][j]
    print(f"\ntotal allocated resources : {allocated}")

    available = [max_resources[i] - allocated[i] for i in range(resources)]
    print(f"total available resources : {available}\n")

    running = [True] * processes
    count = processes
    safe_sequence = []  # List to track the safe execution sequence

    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"process {i + 1} is executing")
                    safe_sequence.append(i + 1)  # Append process number to safe sequence
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("the processes are in an unsafe state.")
            break

        print(f"the process is in a safe state.\navailable resources : {available}\n")

    if safe:
        print("\nSafe Execution Sequence:")
        print(" -> ".join([f"Process {p}" for p in safe_sequence]))

if __name__ == '__main__':
    main()

    
    
    
#number of processes : 5
#number of resources : 3
#maximum resources : 10 7 5

#-- allocated resources for each process --
#process 1 : 0 1 0
#process 2 : 2 0 0
#process 3 : 1 0 0
#process 4 : 1 1 0
#process 5 : 0 0 2

#-- maximum resources for each process --
#process 1 : 7 5 3
#process 2 : 3 2 2
#process 3 : 2 1 1
#process 4 : 1 2 1
#process 5 : 4 3 3
