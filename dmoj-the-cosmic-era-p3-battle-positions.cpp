// Problem: The Cosmic Era P3 - Battle Positions (seed3)
// Problem URL: https://dmoj.ca/problem/seed3
// Submission: 4762899 (https://dmoj.ca/submission/4762899)
// Language: C++20 (CPP20)
// Submitted: 2022-08-10T22:10:16+00:00

#include <iostream>
using namespace std;

int main() {
    int num_stations;
    int min_people;
    int num_waves;
    cin >> num_stations;
    cin >> min_people;
    cin >> num_waves;

    int station_list[num_stations + 1];
    for (int i = 0; i < num_stations + 1; i++) {
        station_list[i] = 0;
    }

    int left;
    int right;
    int num_people;

    for (int i = 0; i < num_waves; i++) {
        cin >> left;
        cin >> right;
        cin >> num_people;

        station_list[left - 1] += num_people;
        station_list[right] -= num_people;
    }

    int counter = 0;

    if (station_list[0] < min_people) {
        counter += 1;
    }

    for (int i = 1; i < num_stations; i++) {
        station_list[i] = station_list[i - 1] + station_list[i];
        if (station_list[i] < min_people) {
            counter += 1;
        }
    }


    cout << counter;

    return 0;
}