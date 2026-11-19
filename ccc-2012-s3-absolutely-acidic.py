# Problem: CCC '12 S3 - Absolutely Acidic (ccc12s3)
# Problem URL: https://dmoj.ca/problem/ccc12s3
# Submission: 4577078 (https://dmoj.ca/submission/4577078)
# Language: PYPY3 (PYPY3)
# Submitted: 2022-05-23T17:51:34+00:00

# CCC '12 S3 - Absolutely Acidic 2

num_readings = int(input())

readings_list = []
readings_dic = {}

for i in range(num_readings):
    temp_input = int(input())

    if temp_input not in readings_list:
        readings_list.append(temp_input)
        readings_dic[temp_input] = 1
    else:
        readings_dic[temp_input] += 1

final_list = []

for i in range(len(readings_list)):
    final_list.append([readings_list[i],readings_dic[readings_list[i]]])

final_list.sort(key = lambda final_list: final_list[1], reverse = True)

frequent_1_list = []
frequent_2_list = []
max_value = final_list[0][1]
min_value = -1

for i in range(len(final_list)):
    if max_value == final_list[i][1]:
        frequent_1_list.append(final_list[i][0])
    else:
        if min_value == -1:
            min_value = final_list[i][1]
            frequent_2_list.append(final_list[i][0])
        elif min_value == final_list[i][1]:
            frequent_2_list.append(final_list[i][0])
        else:
            break

if frequent_2_list == []:
    frequent_2_list = frequent_1_list

frequent_1_list.sort()
frequent_2_list.sort()

if len(frequent_1_list) > 1:
    print(abs(frequent_1_list[0] - frequent_1_list[-1]))
else:
    if (abs(frequent_1_list[0] - frequent_2_list[-1]) > frequent_1_list[-1] - frequent_2_list[0]):
        print(abs(frequent_1_list[0] - frequent_2_list[-1]))
    else:
        print(frequent_1_list[-1] - frequent_2_list[0])