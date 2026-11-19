# Problem: Hackathon (oly20practice25)
# Problem URL: https://dmoj.ca/problem/oly20practice25
# Submission: 4433953 (https://dmoj.ca/submission/4433953)
# Language: PYPY3 (PYPY3)
# Submitted: 2022-03-20T18:40:28+00:00

# Hackathon

import math

num_questions, num_people = list(map(int,input().split()))

people_list = []

for i in range(num_people):
    coding_speed, coding_time, rest_time = list(map(int,input().split()))

    total_questions = 0
    counter = 0
    temp_counter = int(coding_time)
    resting = False
    while total_questions < num_questions:
        counter += 1
        temp_counter -= 1

        if resting == False:
            total_questions += coding_speed
        
        if temp_counter <= 0:
            if resting == True:
                temp_counter = int(coding_time)
                resting = False
            else:
                temp_counter = int(rest_time)
                resting = True
        #print(counter,temp_counter,resting,total_questions)

    print(counter)