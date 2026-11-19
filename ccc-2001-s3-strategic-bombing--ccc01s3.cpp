// Problem: CCC '01 S3 - Strategic Bombing (ccc01s3)
// Problem URL: https://dmoj.ca/problem/ccc01s3
// Submission: 4797159 (https://dmoj.ca/submission/4797159)
// Language: C++20
// Submitted: 2022-08-25T18:02:35+00:00

#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

int print_dic(map<char, vector<char>> dictionary_graph) {
    for (auto element: dictionary_graph)
    {
        cout << element.first << " - ";
        for (int i = 0; i < element.second.size(); i++) {
            cout << element.second[i] << " ";
        }
        cout << endl;
    }
    cout << "----------" << endl;
    return 0 ;
}

bool is_connected(map<char, vector<char>> dictionary_graph) {

    vector<char> queue;
    vector<char> visted;
    bool in_visted;
    queue.push_back('A');

    while (!queue.empty()) {

        in_visted = false;
        for (int i = 0; i < visted.size(); i++) {
            if (queue[0] == visted[i]) {
                in_visted = true;
            }
        }

        if (!in_visted) {
            for (int i = 0; i < dictionary_graph[queue[0]].size(); i++) {
                if (dictionary_graph[queue[0]][i] == 'B') {
                    return true;
                }
                else {
                    queue.push_back(dictionary_graph[queue[0]][i]);
                }
            }
        }
        if (!in_visted) {
            visted.push_back(queue[0]);
        }
        queue.erase(queue.begin() + 0);
    }

    return false;
}

int main() {

    string input = "null";
    int road_counter = 0;
    vector<string> input_array;

    while (input != "**") {
        cin >> input;
        if (input == "**") {
            break;
        }
        input_array.push_back(input);
    }

    for (int a = 0; a < input_array.size(); a++) {
        vector<string> new_input_array(input_array);
        new_input_array.erase(new_input_array.begin() + a);
        map<char, vector<char>> dictionary_graph;

        for (int b = 0; b < new_input_array.size(); b++) {
            input = new_input_array[b];
            bool new_element[2] = {true, true};

            for (auto element: dictionary_graph) {
                for (int i = 0; i < 2; i++) {

                    if (element.first == input[i]) {
                        new_element[i] = false;

                        bool new_char = true;
                        for (int j = 0; j < element.second.size(); j++) {
                            if (element.second[j] == input[1 - i]) {
                                new_char = false;
                            }
                        }

                        if (new_char && input[0] != input[1]) {
                            dictionary_graph[element.first].push_back(input[1 - i]);
                        }
                    }
                }
            }

            for (int i = 0; i < 2; i++) {
                if (new_element[i] && input[0] != input[1]) {
                    dictionary_graph[input[i]];
                    dictionary_graph[input[i]].push_back(input[1 - i]);
                }
            }
        }
        if (!is_connected(dictionary_graph)) {
            cout << input_array[a] << endl;
            road_counter += 1;
        }
    }

    cout << "There are " + to_string(road_counter) + " disconnecting roads." << endl;

    return 0;
}