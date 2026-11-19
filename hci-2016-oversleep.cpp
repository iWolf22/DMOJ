// Problem: HCI '16 - Oversleep (hci16oversleep)
// Problem URL: https://dmoj.ca/problem/hci16oversleep
// Submission: 4898656 (https://dmoj.ca/submission/4898656)
// Language: C++14 (CPP14)
// Submitted: 2022-10-03T00:26:56+00:00

#include <iostream>
#include <string>
#include <queue>
#include <array>

using namespace std;

int main() {

    int rows;
    int cols;

    cin >> rows;
    cin >> cols;

    char matrix[rows][cols];
    queue<array<int, 2>> queue;

    string input;

    for (int i = 0; i < rows; i++) {
        cin >> input;
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = input[j];
            if (matrix[i][j] == 's') {
                queue.push({i, j});
            }
        }
    }

    bool visited[rows][cols];
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            visited[i][j] = false;
        }
    }

    bool found = false;
    int counter = 0;
    int directions[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    int new_x;
    int new_y;
    int loops;

    while (queue.size() != 0) {
        loops = queue.size();
        for (int a = 0; a < loops; a++) {
            if (matrix[queue.front()[0]][queue.front()[1]] == 'e') {
                found = true;
                goto end;
            }
            for (int i = 0; i < 4; i++) {
                new_x = queue.front()[0] + directions[i][0];
                new_y = queue.front()[1] + directions[i][1];
                if (new_x >= 0 && new_x < rows && new_y >= 0 && new_y < cols) {
                    if (visited[new_x][new_y] == false && matrix[new_x][new_y] != 'X') {
                        queue.push({new_x, new_y});
                    }
                }
            }

            visited[queue.front()[0]][queue.front()[1]] = true;
            queue.pop();
        }
        counter += 1;
    }

    end:

    if (found == true) {
        cout << counter - 1 << endl;
    }
    else {
        cout << -1 << endl;
    }

    return 0;
}