// Problem: Hardcore Grinding (grind)
// Problem URL: https://dmoj.ca/problem/grind
// Submission: 4762965 (https://dmoj.ca/submission/4762965)
// Language: C++20 (CPP20)
// Submitted: 2022-08-10T22:41:22+00:00

#include <iostream>
using namespace std;

int main() {

    int num_tasks;
    cin >> num_tasks;
    int time_array[10000000] = {0};
    int left;
    int right;


    for (int i = 0; i < num_tasks; i++) {
        cin >> left;
        cin >> right;
        time_array[left] += 1;
        time_array[right] -= 1;
    }

    int max_val = 0;

    for (int i = 1; i < 10000000; i++) {
        time_array[i] = time_array[i - 1] + time_array[i];
        if (time_array[i] > max_val) {
            max_val = time_array[i];
        }
    }

    cout << max_val;

    return 0;

}