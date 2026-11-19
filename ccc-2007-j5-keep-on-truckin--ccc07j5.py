# Problem: CCC '07 J5 - Keep on Truckin' (ccc07j5)
# Problem URL: https://dmoj.ca/problem/ccc07j5
# Submission: 4576180 (https://dmoj.ca/submission/4576180)
# Language: 
# Submitted: 2022-05-23T03:27:53+00:00

# CCC '07 J5 - Keep on Truckin'

locations_list = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

low_num = int(input())
high_num = int(input())

num_new_stop = int(input())

for i in range(num_new_stop):
    locations_list.append(int(input()))

locations_list.sort()

dp_list = [0 for i in range(len(locations_list))]

dp_list[0] = 1

for i in range(len(locations_list)):
    if dp_list[i] != 0:
        for j in range(i + 1, len(locations_list)):
            if locations_list[j] - locations_list[i] >= low_num and locations_list[j] - locations_list[i] <= high_num:
                dp_list[j] += dp_list[i]

print(dp_list[-1])