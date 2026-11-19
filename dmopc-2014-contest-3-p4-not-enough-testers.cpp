// Problem: DMOPC '14 Contest 3 P4 - Not Enough Testers! (dmopc14c3p4)
// Problem URL: https://dmoj.ca/problem/dmopc14c3p4
// Submission: 4779769 (https://dmoj.ca/submission/4779769)
// Language: C++14 (CPP14)
// Submitted: 2022-08-18T18:10:55+00:00

#include <iostream>
using namespace std;

int quick_factors[128][100001] {0};

int main() {

    int factors_array[100001] = {0};
    for (int i = 1; i < 100001; i++) {
        for (int j = i - 1; j < 100001; j += i) {
            factors_array[j] += 1;
        }
    }

    bool visted_factors[128] = {false};
    for (int i = 0; i < 100000; i++) {
        quick_factors[factors_array[i] - 1][i + 1] += 1;
        visted_factors[factors_array[i] - 1] = true;
    }

    for (int i = 0; i < 128; i++) {
        if (visted_factors[i]) {
            for (int j = 1; j < 100001; j++) {
                quick_factors[i][j] += quick_factors[i][j - 1];
            }
        }
    }

    /*
    for (int i = 0; i < 9; i++) {

        for (int j = 0; j < 30; j++) {
            cout << quick_factors[i][j];
            cout << " ";
        }
        cout << "\n";
    }
    */

    int num_test_cases;
    cin >> num_test_cases;

    int num_factors;
    int left_pointer;
    int right_pointer;

    for (int i = 0; i < num_test_cases; i++) {
        cin >> num_factors;
        cin >> left_pointer;
        cin >> right_pointer;

        if (num_factors > 128) {
            cout << 0 << endl;
        }
        else {
            cout << quick_factors[num_factors - 1][right_pointer] - quick_factors[num_factors - 1][left_pointer - 1] << endl;
        }
    }

    return 0;
}