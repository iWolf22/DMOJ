// Problem: USACO 2019 December Bronze P1 - Cow Gymnastics (usaco19decbronze1)
// Problem URL: https://dmoj.ca/problem/usaco19decbronze1
// Submission: 3913125 (https://dmoj.ca/submission/3913125)
// Language: C++20 (CPP20)
// Submitted: 2021-09-25T20:25:12+00:00

#include <bits/stdc++.h>

using namespace std;

int main() {
	
	int num_events;
	int num_cows;
	int temp;

	cin >> num_events;
	cin >> num_cows;

	int cow_array[num_events][num_cows];
	
	for (int i = 0; i < num_events; i++)
	{
		for (int j = 0; j < num_cows; j++)
		{
			cin >> temp;
			cow_array[i][j] = temp;
		}
	}
	
	int counter;
	counter = 0;

	for (int i = 0; i < num_cows; i++)
	{
		for (int j = 0; j < num_cows; j++)
		{
			if (i != j)
			{
				temp = 0;
				for (int a = 0; a < num_events; a++)
				{
					
					for (int b = 0; b < num_cows; b++)
					{
						if (cow_array[a][b] == i + 1)
						{
							break;
						}
						if (cow_array[a][b] == j + 1)
						{
							temp = 1;
						}
						
					}
				}
				if (temp == 0)
				{
					counter += 1;
				}
			}
		}
	
	}
cout << counter;

}