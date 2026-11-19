// Problem: DMOPC '14 Contest 2 P4 - Deforestation (dmopc14c2p4)
// Problem URL: https://dmoj.ca/problem/dmopc14c2p4
// Submission: 4761203 (https://dmoj.ca/submission/4761203)
// Language: C++20 (CPP20)
// Submitted: 2022-08-09T23:57:41+00:00

#include <iostream>
using namespace std;

int main() {

    int num_trees;
    cin >> num_trees;

    int trees_array[num_trees];
    int psa[num_trees + 1];
    psa[0] = 0;
    for (int i = 0; i < num_trees; i++) {
        cin >> trees_array[i];
        psa[i + 1] = psa[i] + trees_array[i];
    }

    int num_cuts;
    cin >> num_cuts;
    int left_side;
    int right_side;
    int final;

    /*
    for (int i = 0; i < num_trees + 1; i++) {
        cout << to_string(psa[i]) + "\n";
    }
     */

    for (int i = 0; i < num_cuts; i++) {
        cin >> left_side;
        cin >> right_side;
        final = psa[right_side + 1] - psa[left_side];
        cout <<  to_string(final) + "\n";

    }


    return 0;
}