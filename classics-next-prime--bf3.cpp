// Problem: Next Prime (bf3)
// Problem URL: https://dmoj.ca/problem/bf3
// Submission: 4773416 (https://dmoj.ca/submission/4773416)
// Language: C++20 (CPP20)
// Submitted: 2022-08-15T20:28:44+00:00

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
    int num;
    cin >> num;

    int counter = 0;
    while (true) {
        if (isPrime(num + counter) == true) {
            break;
        }
        counter += 1;
    }
    cout << counter + num;
    return 0;
}