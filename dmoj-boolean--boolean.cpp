// Problem: Boolean (boolean)
// Problem URL: https://dmoj.ca/problem/boolean
// Submission: 3697730 (https://dmoj.ca/submission/3697730)
// Language: C++20 (CPP20)
// Submitted: 2021-06-26T16:57:02+00:00

// Your First C++ Program

#include <iostream>
using namespace std;

int main() {
	string word;
	cin >> word;
	int not_counter;
	not_counter = 0;
   	while (word == "not") {
		not_counter += 1;
		cin >> word;
	}
	if (not_counter % 2 == 0) {
		cout << word;
	}
	else {
		if (word == "True") {
			cout << "False";
		}
		else {
			cout << "True";
		}
	}
}