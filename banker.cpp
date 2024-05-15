#include <iostream>
using namespace std;

class BankerAlgo {
public:
    int no_p, no_r;
    int allocate[5][4], max[5][4], need[5][4], available[1][4];

    void input() {
        cout << "Enter the number of processes and resources: ";
        cin >> no_p >> no_r;

        cout << "Enter allocation matrix:\n";
        for (int i = 0; i < no_p; i++)
            for (int j = 0; j < no_r; j++)
                cin >> allocate[i][j];

        cout << "Enter max matrix:\n";
        for (int i = 0; i < no_p; i++)
            for (int j = 0; j < no_r; j++)
                cin >> max[i][j];

        cout << "Enter available matrix:\n";
        for (int j = 0; j < no_r; j++)
            cin >> available[0][j];
    }

    void calc_need() {
        for (int i = 0; i < no_p; i++)
            for (int j = 0; j < no_r; j++)
                need[i][j] = max[i][j] - allocate[i][j];
    }

    bool check(int i) {
        for (int j = 0; j < no_r; j++)
            if (available[0][j] < need[i][j])
                return false;

        return true;
    }

    void issafe() {
        input();
        calc_need();
        bool done[10] = {false};
        int j = 0;
        // Print the Need matrix
        cout << "Need Matrix is:\n";
        for (int i = 0; i < no_p; i++) {
            for (int j = 0; j < no_r; j++) {
                cout << need[i][j] << " ";
            }
            cout << endl;
        }
        cout << "Allocated Processes: ";
        while (j < no_p) {
            bool allocate = false;
            for (int i = 0; i < no_p; i++)
                if (!done[i] && check(i)) {
                    for (int k = 0; k < no_r; k++)
                        available[0][k] = available[0][k] - need[i][k] + max[i][k];

                    cout << i << "-->";
                    allocate = done[i] = true;
                    j++;
                }
            if (!allocate) break;
        }
        if (j == no_p)
            cout << "\nSafely executed!\n";
        else
            cout << "All processes can't be safely executed\n";
    }
};

int main() {
    BankerAlgo banker;
    banker.issafe();
    return 0;
}
