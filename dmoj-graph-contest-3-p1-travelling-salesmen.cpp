// Problem: Graph Contest 3 P1 - Travelling Salesmen (graph3p1)
// Problem URL: https://dmoj.ca/problem/graph3p1
// Submission: 4922733 (https://dmoj.ca/submission/4922733)
// Language: C++14 (CPP14)
// Submitted: 2022-10-10T00:21:29+00:00

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {

    int num_cities;
    int num_roads;

    int city1;
    int city2;

    cin >> num_cities;
    cin >> num_roads;

    vector<int> roads[100000];

    for (int i = 0; i < num_roads; i++) {
        cin >> city1;
        cin >> city2;

        roads[city1].push_back(city2);
        roads[city2].push_back(city1);
    }

    int num_men;
    int input;
    cin >> num_men;

    queue<int> queue;

    for (int i = 0; i < num_men; i++) {
        cin >> input;
        queue.push(input);
    }

    int counter = 0;
    int loops;
    int visited[100000] = {0};

    while (queue.size() != 0) {
        counter += 1;
        loops = queue.size();
        for (int i = 0; i < loops; i++) {
            for (int j = 0; j < roads[queue.front()].size(); j++) {
                if (visited[roads[queue.front()][j]] == 0) {
                    queue.push(roads[queue.front()][j]);
                    visited[roads[queue.front()][j]] = 1;
                }
            }
            //cout << queue.front() << endl;
            visited[queue.front()] = 1;
            queue.pop();
        }

        /*
        for (int i = 0; i < 5; i++) {
            cout << visited[i];
            cout << " ";
        }
        cout << endl;
        */
    }

    cout << counter - 1 << endl;

    return 0;
}