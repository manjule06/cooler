#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int size, disk_size, head;

    // Get user input for array size, disk size, and initial head position
    cout << "Enter the size of the request array: ";
    cin >> size;

    int arr[size];
    cout << "Enter the request array elements: ";
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }

    cout << "Enter the disk size: ";
    cin >> disk_size;

    cout << "Enter the initial position of the head: ";
    cin >> head;

    int seek_count = 0;
    int distance, cur_track;
    vector<int> left, right;
    vector<int> seek_sequence;

    for (int i = 0; i < size; i++) {
        if (arr[i] < head)
            left.push_back(arr[i]);
        if (arr[i] > head)
            right.push_back(arr[i]);
    }

    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());

    for (int i = 0; i < right.size(); i++) {
        cur_track = right[i];
        seek_sequence.push_back(cur_track);
        distance = abs(cur_track - head);
        seek_count += distance;
        head = cur_track;
    }

    seek_count += abs(head - left[0]);
    head = left[0];

    for (int i = 0; i < left.size(); i++) {
        cur_track = left[i];
        seek_sequence.push_back(cur_track);
        distance = abs(cur_track - head);
        seek_count += distance;
        head = cur_track;
    }

    cout << "Total number of seek operations = " << seek_count << endl;
    cout << "Seek Sequence is" << endl;

    for (int i = 0; i < seek_sequence.size(); i++) {
        cout << seek_sequence[i] << endl;
    }

    return 0;
}
