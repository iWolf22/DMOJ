// Problem: An Animal Contest 7 P1 - Squirrnect 4 (aac7p1)
// Problem URL: https://dmoj.ca/problem/aac7p1
// Submission: 4835733 (https://dmoj.ca/submission/4835733)
// Language: C++14
// Submitted: 2022-09-13T02:10:58+00:00

#include <iostream>

using namespace std;

int main() {
    int w;
    int h;
    int num_boards;
    cin >> num_boards;
    for (int i = 0; i < num_boards; i++) {
        cin >> w;
        cin >> h;

        if ((h >= 1 && w >= 7) || (h >= 2 && w >= 4) || (h >= 4 && w >= 2)) {
            cout << "good" << endl;
        }
        else {
            cout << "bad" << endl;
        }
    }

    return 0;
}