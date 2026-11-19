// Problem: CCC '21 J4 - Arranging Books (ccc21j4)
// Problem URL: https://dmoj.ca/problem/ccc21j4
// Submission: 4875485 (https://dmoj.ca/submission/4875485)
// Language: C++14 (CPP14)
// Submitted: 2022-09-25T23:53:52+00:00

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {

    int num_s = 0;
    int num_m = 0;
    int num_l = 0;

    int move_counter = 0;

    string input_string;
    cin >> input_string;

    char book_array[input_string.length()];

    for (int i = 0; i < input_string.length(); i++) {
        if (input_string[i] == 'L') {
            num_l += 1;
        }
        else if (input_string[i] == 'M') {
            num_m += 1;
        }
        else {
            num_s += 1;
        }

        book_array[i] = input_string[i];
    }

    int s_in_l = 0;
    int m_in_l = 0;
    int s_in_m = 0;
    int l_in_m = 0;
    int l_in_s = 0;
    int m_in_s = 0;

    for (int i = 0; i < num_l; i++) {
        if (book_array[i] == 'S') {
            s_in_l += 1;
        }
        if (book_array[i] == 'M') {
            m_in_l += 1;
        }
    }

    for (int i = num_l; i < num_l + num_m; i++) {
        if (book_array[i] == 'S') {
            s_in_m += 1;
        }
        if (book_array[i] == 'L') {
            l_in_m += 1;
        }
    }

    for (int i = num_l + num_m; i < num_l + num_m + num_s; i++) {
        if (book_array[i] == 'L') {
            l_in_s += 1;
        }
        if (book_array[i] == 'M') {
            m_in_s += 1;
        }
    }

    int dif;
    dif = min(s_in_l, l_in_s);
    move_counter += dif;
    s_in_l -= dif;
    l_in_s -= dif;
    dif = min(m_in_l, l_in_m);
    move_counter += dif;
    m_in_l -= dif;
    l_in_m -= dif;
    dif = min(m_in_s, s_in_m);
    move_counter += dif;
    m_in_s -= dif;
    s_in_m -= dif;

    move_counter += m_in_l * 2;
    move_counter += s_in_l * 2;

    cout << move_counter << endl;

    return 0;
}