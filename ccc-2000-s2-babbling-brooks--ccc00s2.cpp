// Problem: CCC '00 S2 - Babbling Brooks (ccc00s2)
// Problem URL: https://dmoj.ca/problem/ccc00s2
// Submission: 4791173 (https://dmoj.ca/submission/4791173)
// Language: C++20 (CPP20)
// Submitted: 2022-08-22T22:09:35+00:00

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {

    int num_rivers;
    cin >> num_rivers;
    vector<double> rivers_list;
    double input_int;

    for (int i = 0; i < num_rivers; i++) {
        cin >> input_int;
        rivers_list.push_back(input_int);
    }

    int input_command = 0;
    double river_num;
    double river_percent;

    while (input_command != 77) {
        cin >> input_command;
        if (input_command == 99) {
            cin >> river_num;
            cin >> river_percent;
            rivers_list.insert(rivers_list.begin() + river_num, ((100 - river_percent) / 100) * rivers_list[river_num - 1]);
            rivers_list[river_num - 1] = rivers_list[river_num - 1] * (river_percent / 100);
        }
        if (input_command == 88) {
            cin >> river_num;
            rivers_list[river_num - 1] = rivers_list[river_num - 1] + rivers_list[river_num];
            rivers_list.erase(rivers_list.begin() + river_num);
        }
    }

    for (int i = 0; i < rivers_list.size(); i++) {
        cout << to_string(int(rivers_list[i])) + " ";
    }

    return 0;
}