#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int disk_size;

void SCAN(vector<int> arr, int head, string direction)
{
    int seek_count = 0;
    int distance, cur_track;
    vector<int> left, right, seek_sequence;

    if (direction == "left")
        left.push_back(0);
    else if (direction == "right")
        right.push_back(disk_size - 1);

    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] < head)
            left.push_back(arr[i]);
        if (arr[i] > head)
            right.push_back(arr[i]);
    }

    sort(left.begin(), left.end());
    sort(right.begin(), right.end());

    int run = 2;
    while (run-- > 0)
    {
        if (direction == "left")
        {
            for (int i = left.size() - 1; i >= 0; i--)
            {
                cur_track = left[i];
                seek_sequence.push_back(cur_track);
                distance = abs(cur_track - head);
                seek_count += distance;
                head = cur_track;
            }
            direction = "right";
        }
        else if (direction == "right")
        {
            for (int i = 0; i < right.size(); i++)
            {
                cur_track = right[i];
                seek_sequence.push_back(cur_track);
                distance = abs(cur_track - head);
                seek_count += distance;
                head = cur_track;
            }
            direction = "left";
        }
    }

    cout << "Total number of seek operations = " << seek_count << endl;
    cout << "Seek Sequence is" << endl;
    for (int i = 0; i < seek_sequence.size(); i++)
    {
        cout << seek_sequence[i] << endl;
    }
}

int main()
{
    int size, head;
    cout << "Enter the number of requests: ";
    cin >> size;
    vector<int> arr(size);

    cout << "Enter the requests:" << endl;
    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }

    cout << "Enter the initial head position: ";
    cin >> head;

    cout << "Enter the disk size: ";
    cin >> disk_size;

    string direction;
    cout << "Enter the direction of head movement (left or right): ";
    cin >> direction;

    SCAN(arr, head, direction);

    return 0;
}