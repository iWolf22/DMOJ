// Problem: CCC '19 J3 - Cold Compress (ccc19j3)
// Problem URL: https://dmoj.ca/problem/ccc19j3
// Submission: 4922368 (https://dmoj.ca/submission/4922368)
// Language: C++14 (CPP14)
// Submitted: 2022-10-09T22:59:53+00:00

#include <iostream>
#include <string>

using namespace std;

int main() {

    int num;
    string input;
    char prev;
    int counter;
    cin >> num;

    for (int i = 0; i < num; i++) {
        cin >> input;
        prev = input[0];
        counter = 0;
        for (int j = 0; j < input.length() + 1; j++) {
            if (prev == input[j]) {
                counter += 1;
            }
            else {
                cout << counter;
                cout << " ";
                cout << prev;
                cout << " ";
                counter = 1;
                prev = input[j];
            }
        }
        cout << endl;
    }

    return 0;
}