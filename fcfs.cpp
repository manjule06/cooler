#include <iostream>
using namespace std;

int main()
{
    int no_of_processes;
    int total_waiting_time = 0, total_turn_around_time = 0;
    float average_waiting_time, average_turn_around_time;
    int current_time = 0;

    cout << "Enter the number of processes: ";
    cin >> no_of_processes;

    int arrival_time[no_of_processes], burst_time[no_of_processes];
    int completion_time[no_of_processes], turn_around_time[no_of_processes], waiting_time[no_of_processes];

    for (int i = 0; i < no_of_processes; i++)
    {
        cout << "Enter the arrival time and burst time of process " << i + 1 << ": ";
        cin >> arrival_time[i] >> burst_time[i];
    }

    for (int i = 0; i < no_of_processes; i++)
    {
        if (current_time < arrival_time[i])
        {
            current_time = arrival_time[i];
        }
        current_time += burst_time[i];
        completion_time[i] = current_time;
        turn_around_time[i] = completion_time[i] - arrival_time[i];
        waiting_time[i] = turn_around_time[i] - burst_time[i];
        total_waiting_time += waiting_time[i];
        total_turn_around_time += turn_around_time[i];
    }

    average_waiting_time = (float)total_waiting_time / no_of_processes;
    average_turn_around_time = (float)total_turn_around_time / no_of_processes;

    cout << "Process\tArrival Time\tBurst Time\tCompletion Time\tTurn Around Time\tWaiting Time\n";
    for (int i = 0; i < no_of_processes; i++)
    {
        cout << i + 1 << "\t\t" << arrival_time[i] << "\t\t" << burst_time[i] << "\t\t" << completion_time[i] << "\t\t" << turn_around_time[i] << "\t\t" << waiting_time[i] << "\n";
    }

    cout << "Average Waiting Time: " << average_waiting_time << "\n";
    cout << "Average Turn Around Time: " << average_turn_around_time << "\n";

    return 0;
}