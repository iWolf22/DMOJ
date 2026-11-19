// Problem: CCC '17 J4 - Favourite Times (ccc17j4)
// Problem URL: https://dmoj.ca/problem/ccc17j4
// Submission: 4965047 (https://dmoj.ca/submission/4965047)
// Language: C++14
// Submitted: 2022-10-23T23:03:39+00:00

#include <iostream>
#include <cmath>

using namespace std;

int main() {

    int min;
    cin >> min;

    int hour_1 = 1;
    int hour_2 = 2;
    int min_1 = 0;
    int min_2 = 0;
    int counter = floor(min / 720) * 31;
    
    min = min % 720;

    for (int i = 0; i < min; i++) {
        min_2 += 1;
        if (min_2 >= 10) {
            min_2 = 0;
            min_1 += 1;
        }
        if (min_1 >= 6) {
            min_1 = 0;
            hour_2 += 1;
        }
        if (hour_2 >= 10) {
            hour_2 = 0;
            hour_1 += 1;
        }
        if (hour_2 >= 3 && hour_1 == 1) {
            hour_2 = 1;
            hour_1 = 0;
        }

        if ((min_1 - min_2 == hour_2 - min_1 && hour_2 - min_1 == hour_1 - hour_2) || (hour_1 == 0 && (min_1 - min_2 == hour_2 - min_1))) {
            counter += 1;
        }

        /*
        cout << hour_1;
        cout << hour_2;
        cout << ":";
        cout << min_1;
        cout << min_2;
        cout << endl;
         */

    }

    cout << counter;

    return 0;
}