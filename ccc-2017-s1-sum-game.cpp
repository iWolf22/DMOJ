// Problem: CCC '17 S1 - Sum Game (ccc17s1)
// Problem URL: https://dmoj.ca/problem/ccc17s1
// Submission: 4761143 (https://dmoj.ca/submission/4761143)
// Language: C++20 (CPP20)
// Submitted: 2022-08-09T23:25:16+00:00

#include <iostream>
using namespace std;

int main() {

    int num_games;
    cin >> num_games;

    int team1[num_games];
    int team2[num_games];

    for (int i = 0; i < num_games; i++) {
        cin >> team1[i];
    }
    for (int i = 0; i < num_games; i++) {
        cin >> team2[i];
    }

    int counter1 = 0;
    int counter2 = 0;

    int largest = 0;

    for (int i = 0; i < num_games; i++) {
        if (counter1 == counter2) {
            largest = i;
        }
        counter1 += team1[i];
        counter2 += team2[i];

    }

    if (counter1 == counter2) {
        largest = num_games;
    }

    cout << largest;
    return 0;
}