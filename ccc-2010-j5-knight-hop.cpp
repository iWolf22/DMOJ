// Problem: CCC '10 J5 - Knight Hop (ccc10j5)
// Problem URL: https://dmoj.ca/problem/ccc10j5
// Submission: 4876878 (https://dmoj.ca/submission/4876878)
// Language: C++14 (CPP14)
// Submitted: 2022-09-26T14:11:06+00:00

#include <iostream>
#include <vector>

using namespace std;

int main() {

    int x_start;
    int y_start;

    int x_final;
    int y_final;

    cin >> x_start;
    cin >> y_start;

    cin >> x_final;
    cin >> y_final;

    vector<pair<int, int>> queue;
    int visted[8][8] = {0};

    int knight_moves[8][2] = {{2,1},{1,2},{-2,1},{-1,2},{2,-1},{1,-2},{-2,-1},{-1,-2}};

    queue.push_back({x_start, y_start});

    int loops;
    int num_moves = 0;

    while (queue.size() != 0) {

        loops = queue.size();

        for (int i = 0; i < loops; i++) {

            if (queue[0].first == x_final && queue[0].second == y_final) {
                //cout << "end" << endl;
                goto end;
            }

            for (int j = 0; j < 8; j++) {

                if (-1 < queue[0].first + knight_moves[j][0] - 1 && queue[0].first + knight_moves[j][0] - 1 < 8 && -1 < queue[0].second + knight_moves[j][1] - 1 && queue[0].second + knight_moves[j][1] - 1 < 8) {
                    if (visted[queue[0].first + knight_moves[j][0] - 1][queue[0].second + knight_moves[j][1] - 1] == 0) {
                        queue.push_back({queue[0].first + knight_moves[j][0], queue[0].second + knight_moves[j][1]});
                    }
                }
            }

            visted[queue[0].first - 1][queue[0].second - 1] = num_moves + 1;
            queue.erase(queue.begin() + 0);

        }

        /*
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                cout << visted[i][j];
                cout << " ";
            }
            cout << endl;
        }
        cout << "---------------" << endl;
         */

        num_moves += 1;
    }

    end:

    cout << num_moves << endl;

    return 0;
}