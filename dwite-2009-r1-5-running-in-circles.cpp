// Problem: DWITE '09 R1 #5 - Running In Circles (dwite09c1p5)
// Problem URL: https://dmoj.ca/problem/dwite09c1p5
// Submission: 4943940 (https://dmoj.ca/submission/4943940)
// Language: C++14 (CPP14)
// Submitted: 2022-10-16T23:55:31+00:00

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<int> adj[101];
int dis[101] = {-1};
int max_loops = 0;

int dfs(int current) {

    for (int i = 0; i < adj[current].size(); i++) {
        if (dis[adj[current][i]] == -1) {
            dis[adj[current][i]] = dis[current] + 1;
            dfs(adj[current][i]);
        }
        else {
            if (max_loops < abs(dis[current] - dis[adj[current][i]]) + 1) {
                max_loops = abs(dis[current] - dis[adj[current][i]]) + 1;
            }
        }
    }

    return 0;
}

int main() {

    int num_roads;
    int road1;
    int road2;

    for (int i = 0; i < 5; i++) {
        cin >> num_roads;

        for (int a = 0; a < 101; a++) {
            adj[a].clear();
        }

        fill(dis, dis + 101, -1);

        for (int j = 0; j < num_roads; j++) {
            cin >> road1;
            cin >> road2;

            adj[road1].push_back(road2);
        }

        max_loops = 0;

        for (int j = 0; j < 101; j++) {
            if (dis[j] == -1) {
                dis[j] += 1;
                dfs(j);
            }
        }

        cout << max_loops << endl;
    }

    return 0;
}