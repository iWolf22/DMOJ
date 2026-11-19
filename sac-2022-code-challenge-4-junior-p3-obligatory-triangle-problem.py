# Problem: SAC '22 Code Challenge 4 Junior P3 - Obligatory Triangle Problem (sac22cc4jp3)
# Problem URL: https://dmoj.ca/problem/sac22cc4jp3
# Submission: 4478006 (https://dmoj.ca/submission/4478006)
# Language: Python (PY3)
# Submitted: 2022-04-03T21:24:41+00:00

# SAC '22 Code Challenge 4 Junior P3 - Obligatory Triangle Problem

import math

num_points, closest_angles = list(map(int,input().split()))

angles_distance = math.inf
min_angle_distance = math.inf
min_angle_index = "null"

for i in range(num_points):
    x_point, y_point = list(map(int,input().split()))

    if (x_point == 0 or y_point == 0):
        if (x_point == 0):
            if (y_point > 0):
                angles_distance = 90
            else:
                angles_distance = 270
        else:
            if (x_point > 0):
                angles_distance = 0
            else:
                angles_distance = 180
    else:
        if (x_point >= 0 and y_point >= 0):
            angles_distance = (math.degrees(math.atan(y_point / x_point)))
        elif (x_point <= 0 and y_point >= 0):
            angles_distance = (180 + math.degrees(math.atan(y_point / x_point)))
        elif (x_point <= 0 and y_point <= 0):
            angles_distance = (180 + math.degrees(math.atan(y_point / x_point)))
        elif (x_point >= 0 and y_point <= 0):
            angles_distance = (360 + math.degrees(math.atan(y_point / x_point)))
        else:
            print("error")


    if abs(angles_distance - closest_angles) < min_angle_distance:
        min_angle_distance = abs(angles_distance - closest_angles)
        min_angle_index = i

    if (360 - closest_angles) + angles_distance < min_angle_distance:
        min_angle_distance = (360 - closest_angles) + angles_distance
        min_angle_index = i

    #print(abs(angles_distance - closest_angles) , (360 - closest_angles) + angles_distance)

print(min_angle_index + 1)