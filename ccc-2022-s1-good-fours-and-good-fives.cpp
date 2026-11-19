// Problem: CCC '22 S1 - Good Fours and Good Fives (ccc22s1)
// Problem URL: https://dmoj.ca/problem/ccc22s1
// Submission: 4835799 (https://dmoj.ca/submission/4835799)
// Language: C++14 (CPP14)
// Submitted: 2022-09-13T02:40:22+00:00

#include <iostream>
#include <cmath>

using namespace std;

int main() {

    int input_num;
    cin >> input_num;

    int num_block = floor(input_num / 20);
    int num_loose = input_num % 20;

    int counter = 0;
    if (num_block >= 1) {
        num_block -= 1;
        counter += num_block;
        num_loose += 20;
    }

    for (int i = 0; i < ceil(num_loose / 4) + 1; i++) {
        /*
        cout << num_loose - (4 * i);
        cout << " - ";
        cout << num_loose - (5 * i);
        cout << endl;
         */
        if ((num_loose - (4 * i)) % 5 == 0 && num_loose - (4 * i) / 5 > 0) {
            counter += 1;
        }
        /*
        if ((num_loose - (5 * i)) % 4 == 0 && num_loose - (5 * i) / 4 > 0) {
            cout << 2 << endl;
        }
        if (((num_loose - (4 * i)) % 5 == 0 && num_loose - (4 * i) / 5 > 0) || ((num_loose - (5 * i)) % 4 == 0 && num_loose - (5 * i) / 4 > 0)) {
            counter += 1;
        }
        */
    }
    /*
    cout << num_block << endl;
    cout << num_loose << endl;
    */
    cout << counter << endl;

    return 0;
}