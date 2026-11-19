// Problem: DWITE '11 R4 #2 - Prime Time (dwite11c4p2)
// Problem URL: https://dmoj.ca/problem/dwite11c4p2
// Submission: 4778461 (https://dmoj.ca/submission/4778461)
// Language: C++20 (CPP20)
// Submitted: 2022-08-18T00:43:24+00:00

#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {

    vector<int> primes_list;

    for (int i = 1; i < 10000; i += 2) {
        primes_list.push_back(i);
    }

    for (int i = 1; i < primes_list.size(); i++) {
        for (int j = i + 1; j < primes_list.size(); j++) {
            if (primes_list[j] % primes_list[i] == 0) {
                primes_list.erase(primes_list.begin() + j);
            }
        }
    }

    primes_list[0] = 2;
    int input_num;
    bool first_loop;

    for (int i = 0; i < 5; i++) {
        cin >> input_num;
        int factors_array[primes_list.size()] = { 0 };
        for (int j = 1; j < input_num + 1; j++) {
            int temp_num = j;
            for (int a = 0; a < primes_list.size(); a++) {
                while (temp_num % primes_list[a] == 0) {
                    temp_num /= primes_list[a];
                    factors_array[a] += 1;
                }
                if (temp_num == 0) {
                    break;
                }
            }
        }
        first_loop = true;
        for (int j = 0; j < primes_list.size(); j++) {
            if (factors_array[j] != 0) {
                if (first_loop == true) {
                    first_loop = false;
                }
                else {
                    cout << " * ";
                }
                cout << to_string(primes_list[j]) + "^" + to_string(factors_array[j]);
            }
        }
        cout << endl;
    }

    return 0;
}