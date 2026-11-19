// Problem: CCC '19 S2 - Pretty Average Primes (ccc19s2)
// Problem URL: https://dmoj.ca/problem/ccc19s2
// Submission: 4766295 (https://dmoj.ca/submission/4766295)
// Language: C++20 (CPP20)
// Submitted: 2022-08-12T17:49:19+00:00

#include <iostream>
#include <cmath>
using namespace std;

int isPrime(int num)
{
    if (num == 1) {
        return false;
    }
    if (num == 2) {
        return true;
    }
    if (num % 2 == 0) {
        return false;
    }
    for (int i = 3; i < sqrt(num) + 1; i += 2) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}


int main()
{
    int num_test_cases;
    cin >> num_test_cases;

    int input_num;

    for (int i = 0; i < num_test_cases; i++) {
        cin >> input_num;

        for (int j = 1; j < input_num + 1; j++) {
            if (isPrime(j) == true && isPrime(input_num * 2 - j) == true) {
                cout << to_string(j) + " " + to_string(input_num * 2 - j) + "\n";
                break;
            }
        }
    }

    return 0;
}