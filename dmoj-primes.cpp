// Problem: Primes (primes1)
// Problem URL: https://dmoj.ca/problem/primes1
// Submission: 4773408 (https://dmoj.ca/submission/4773408)
// Language: C++20 (CPP20)
// Submitted: 2022-08-15T20:23:17+00:00

#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {

    int num_primes;
    cin >> num_primes;

    vector<int> primes_list;

    for (int i = 1; i < 10000; i += 2) {
        primes_list.push_back(i);
    }

    if (num_primes != 0) {
        cout << "2\n";
    }

    for (int i = 1; i < primes_list.size(); i++) {
        for (int j = i + 1; j < primes_list.size(); j++) {
            if (primes_list[j] % primes_list[i] == 0) {
                primes_list.erase(primes_list.begin() + j);
            }
        }
    }

    for (int i = 1; i < num_primes; i++) {
        cout << primes_list[i];
        cout << "\n";
    }

    return 0;
}