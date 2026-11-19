// Problem: ECOO '19 R1 P1 - Free Shirts (ecoo19r1p1)
// Problem URL: https://dmoj.ca/problem/ecoo19r1p1
// Submission: 3945746 (https://dmoj.ca/submission/3945746)
// Language: C++20 (CPP20)
// Submitted: 2021-10-10T21:59:20+00:00

#include <bits/stdc++.h>

using namespace std;

int main() {
	
	int num_shirts;
	int num_clean_shirts;
	int num_events;
	int num_days;
	int counter;
	int temp;


	for (int i = 0; i < 10; i++)
	{
		cin >> num_shirts;
		cin >> num_events;
		cin >> num_days;
		int events[num_days];
		for (int j = 0; j < num_days; j++)
		{
			events[j] = 0;
		}

		for (int j = 0; j < num_events; j++)
		{
			cin >> temp;
			events[temp - 1] += 1;
		}

		counter = 0;
		num_clean_shirts = num_shirts - 1 + 1;
		for (int j = 0; j < num_days; j++)
		{
			if (num_clean_shirts == 0)
			{
				num_clean_shirts = num_shirts - 1 + 1;
				counter += 1;
			}
			num_clean_shirts -= 1;
			num_clean_shirts += events[j];
			num_shirts += events[j];
		}
		cout << counter;
		cout << "\n";
	}	
}