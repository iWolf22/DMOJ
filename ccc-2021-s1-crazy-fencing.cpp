// Problem: CCC '21 S1 - Crazy Fencing (ccc21s1)
// Problem URL: https://dmoj.ca/problem/ccc21s1
// Submission: 3901622 (https://dmoj.ca/submission/3901622)
// Language: C++20 (CPP20)
// Submitted: 2021-09-19T17:52:40+00:00

#include <bits/stdc++.h>

using namespace std;

int main() {
	
	int num;
	cin >> num;
	double array1[num + 1];
	double array2[num];
	double temp;

	for (int i = 0; i < num + 1; i++) {
		cin >> temp;
		array1[i] = temp;
	}

	for (int i = 0; i < num; i++) {
		cin >> temp;
		array2[i] = temp;
	}
	
	double counter = 0;	

	for (int i = 0; i < num; i++) {
		counter += ((array1[i] + array1[i + 1]) * array2[i]) / 2;
	}
	
	cout << fixed << setprecision(1) << counter;


}