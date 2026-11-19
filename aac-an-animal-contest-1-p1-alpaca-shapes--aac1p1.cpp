// Problem: An Animal Contest 1 P1 - Alpaca Shapes (aac1p1)
// Problem URL: https://dmoj.ca/problem/aac1p1
// Submission: 3765278 (https://dmoj.ca/submission/3765278)
// Language: C++20 (CPP20)
// Submitted: 2021-07-26T03:34:13+00:00

#include <bits/stdc++.h>

using namespace std;

int main() {
	int num1;
	int num2;
	cin >> num1;
	cin >> num2;
	if (num1 * num1 > num2 * num2 * 3.1415) {
		cout << "SQUARE";
	}
	else {
		cout << "CIRCLE";
	}
}