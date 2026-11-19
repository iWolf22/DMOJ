// Problem: CCC '03 S3 - Floor Plan (ccc03s3)
// Problem URL: https://dmoj.ca/problem/ccc03s3
// Submission: 5301405 (https://dmoj.ca/submission/5301405)
// Language: C++20
// Submitted: 2023-02-08T19:56:55+00:00

#include <iostream>
#include <queue>
#include <array>
#include <algorithm>

using namespace std;

int main() {

    int num_boards;
    int cols;
    int rows;

    cin >> num_boards;
    cin >> rows;
    cin >> cols;

    char matrix[rows][cols];

    char temp_char;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> temp_char;
            matrix[i][j] = temp_char;
        }
    }

    bool visited[rows][cols];

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            visited[i][j] = false;
        }
    }

    int directions[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    queue<array<int, 2>> queue;
    vector<int> rooms;
    int new_x;
    int new_y;

    for (int x = 0; x < rows; x++) {
        for (int y = 0; y < cols; y++) {
            if (matrix[x][y] == '.' && !visited[x][y]) {
                queue.push({x,y});
                int counter = 1;

                while (queue.size() != 0) {
                    for (int i = 0; i < 4; i++) {
                        new_x = queue.front()[0] + directions[i][0];
                        new_y = queue.front()[1] + directions[i][1];
                        if (new_x >= 0 && new_x < rows && new_y >= 0 && new_y < cols) {
                            if (matrix[new_x][new_y] == '.' && !visited[new_x][new_y]) {
                                queue.push({new_x, new_y});
                                visited[new_x][new_y] = true;
                                counter += 1;
                            }
                        }
                    }
                    visited[queue.front()[0]][queue.front()[1]] = true;
                    queue.pop();
                }

                rooms.push_back(counter);

            }
        }
    }

    sort(rooms.begin(), rooms.end(), greater<int>());

    int counter = 0;

    for (int i = 0; i < rooms.size(); i++) {
        num_boards -= rooms[i];
        if (num_boards >= 0) {
            counter += 1;
        }
        else {
            num_boards += rooms[i];
            break;
        }
    }



    cout << counter;
    if (counter == 1) {
        cout << " room, ";
    }
    else {
        cout << " rooms, ";
    }
    cout << num_boards;
    cout << " square metre(s) left over" << endl;

    return 0;
}