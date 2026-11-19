// Problem: GFSSOC '14 Winter J4 - Tic Tac Moe! (gfssoc1j4)
// Problem URL: https://dmoj.ca/problem/gfssoc1j4
// Submission: 3694986 (https://dmoj.ca/submission/3694986)
// Language: C++20 (CPP20)
// Submitted: 2021-06-24T17:31:25+00:00

#include <iostream>
using namespace std;

int main() {
	string string1;
	string string2;
	string string3;
	cin >> string1;
	cin >> string2;
	cin >> string3;
	int bool1;
	int bool2;

	bool1 = 0;
	bool2 = 0;
	
	string array[3] = {string1,string2,string3};
	
	
	for (int i = 0; i < 3; i++) {
		if (array[i][0] == 'O' && array[i][1] == 'O' && array[i][2] == 'O') {
			bool1 = 1;
		}
	}
	
	for (int i = 0; i < 3; i++) {
		if (array[0][i] == 'O' && array[1][i] == 'O' && array[2][i] == 'O') {
			bool1 = 1;
		}
	
	}
	

	for (int i = 0; i < 3; i++) {
		if (array[i][0] == 'X' && array[i][1] == 'X' && array[i][2] == 'X') {
			bool2 = 1;
		}
	}
	
	for (int i = 0; i < 3; i++) {
		if (array[0][i] == 'X' && array[1][i] == 'X' && array[2][i] == 'X') {
			bool2 = 1;
		}
	}

	if (array[0][0] == 'X' && array[1][1] == 'X' && array[2][2] == 'X') {
		bool2 = 1;
	}

	if (array[0][2] == 'X' && array[1][1] == 'X' && array[2][0] == 'X') {
		bool2 = 1;
	}

	if (array[0][0] == 'O' && array[1][1] == 'O' && array[2][2] == 'O') {
		bool1 = 1;
	}

	if (array[0][2] == 'O' && array[1][1] == 'O' && array[2][0] == 'O') {
		bool1 = 1;
	}

	if (bool1 == 1 && bool2 == 1) {
		cout << "Error, redo";
	}
	else if (bool1 == 0 && bool2 == 0) {
		cout << "Tie";
	}
	else if (bool1 == 0 && bool2 == 1) {
		cout << "Timothy";
	}
	else {
		cout << "Griffy";
	}
}