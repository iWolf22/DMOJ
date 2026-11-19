// Problem: CCC '21 S2 - Modern Art (ccc21s2)
// Problem URL: https://dmoj.ca/problem/ccc21s2
// Submission: 4875594 (https://dmoj.ca/submission/4875594)
// Language: C++20 (CPP20)
// Submitted: 2022-09-26T00:20:49+00:00

#include <iostream>
#include <vector>

using namespace std;

int main() {

    int num_cols;
    int num_rows;

    cin >> num_rows;
    cin >> num_cols;

    vector<int> cols_list(num_cols, 0);
    vector<int> rows_list(num_rows,0);

    int num_input;
    cin >> num_input;

    char input1;
    int input2;

    for (int i = 0; i < num_input; i++) {
        cin >> input1;
        cin >> input2;

        if (input1 == 'C') {
            cols_list[input2 - 1] += 1;
        }
        else {
            rows_list[input2 - 1] += 1;
        }
    }

    int gold_counter = 0;

    for (int x = 0; x < num_cols; x++) {
        for (int y = 0; y < num_rows; y++) {
            if ((cols_list[x] + rows_list[y]) % 2 == 1) {
                gold_counter += 1;
            }
        }
    }
    

    cout << gold_counter << endl;

    return 0;
}