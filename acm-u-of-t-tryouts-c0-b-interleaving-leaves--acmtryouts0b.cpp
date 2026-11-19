// Problem: ACM U of T Tryouts C0 B - Interleaving Leaves (acmtryouts0b)
// Problem URL: https://dmoj.ca/problem/acmtryouts0b
// Submission: 3685682 (https://dmoj.ca/submission/3685682)
// Language: C++20 (CPP20)
// Submitted: 2021-06-19T00:57:40+00:00

#include <iostream>
#include <string>
#include <list>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int num;
 	cin >> num;
	int num1;
	string string1;
	string string2;
	for (int i = 0; i < num; i++) {
		string string3("");
		cin >> num1;
		cin >> string1;
		cin >> string2;
		for (int j = 0; j < num1; j++) {
			string3.push_back(string1[j]);
			string3.push_back(string2[j]);
		}
		reverse(string3.begin(),string3.end());
		cout << string3 << "\n";
	}
		
 	return 0;
}