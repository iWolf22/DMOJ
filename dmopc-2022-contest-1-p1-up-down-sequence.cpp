// Problem: DMOPC '22 Contest 1 P1 - Up-down Sequence (dmopc22c1p1)
// Problem URL: https://dmoj.ca/problem/dmopc22c1p1
// Submission: 4944063 (https://dmoj.ca/submission/4944063)
// Language: C++14 (CPP14)
// Submitted: 2022-10-17T00:33:10+00:00

#include <iostream>

using namespace std;

int main() {

    int num_cases;
    int num_input;
    int input1;
    int input2;
    bool up_down;
    bool down_up;

    cin >> num_cases;

    for (int i = 0; i < num_cases; i++) {
        cin >> num_input;
        int alt_array[num_input - 1];

        cin >> input1;

        for (int j = 0; j < num_input - 1; j++) {
            input2 = input1;
            cin >> input1;

            if (input1 == 0 || input2 == 0) {
                alt_array[j] = -1;
            }
            else {
                if (input1 == input2) {
                    alt_array[j] = 2;
                }
                else if (input1 > input2) {
                    alt_array[j] = 1;
                }
                else {
                    alt_array[j] = 0;
                }
            }
        }

        up_down = true;
        down_up = true;

        for (int j = 0; j < num_input - 1; j++) {
            if (alt_array[j] == 2) {
                up_down = false;
                down_up = false;
            }
            if (j % 2 == 0 && alt_array[j] == 0 || j % 2 == 1 && alt_array[j] == 1) {
                up_down = false;
            }
            if (j % 2 == 1 && alt_array[j] == 0 || j % 2 == 0 && alt_array[j] == 1) {
                down_up = false;
            }
        }

        if (down_up == true || up_down == true) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }

    return 0;
}