// Problem: Another Contest 8 Problem 2 - Unnecessary Trash Push (acc8p2)
// Problem URL: https://dmoj.ca/problem/acc8p2
// Submission: 3912535 (https://dmoj.ca/submission/3912535)
// Language: C++20 (CPP20)
// Submitted: 2021-09-25T16:06:34+00:00

#include <bits/stdc++.h>

using namespace std;

int main() {
	
	int num;
	int num_days;
	int garbage_cap;
	int garbage_amount;
	int temp_garbage;
	int take_out_counter;
	cin >> num;
	for (int i = 0; i < num; i ++) 
	{
		cin >> num_days;
		cin >> garbage_cap;
		temp_garbage = 0;
		garbage_amount = 0;
		take_out_counter = 0;
		for (int j = 0; j < num_days; j++)
		{
			cin >> temp_garbage;
			garbage_amount += temp_garbage;
			if (garbage_amount >= garbage_cap)
			{
				take_out_counter += 1;
				garbage_amount = 0;
			}
		}
		cout << take_out_counter;
		cout << "\n";
		
	}

}