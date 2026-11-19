# Problem: CCC '12 S1 - Don't pass me the ball! (ccc12s1)
# Problem URL: https://dmoj.ca/problem/ccc12s1
# Submission: 4576836 (https://dmoj.ca/submission/4576836)
# Language: Python (PY3)
# Submitted: 2022-05-23T16:11:03+00:00

# CCC '12 S1 - Don't pass me the ball!

counter = 0

def recursive_call(jersey_num,iteration):
    global counter
    if iteration == 1:
        counter += 1
    else:
        for i in range(iteration - 1,jersey_num):
            recursive_call(i,iteration - 1)

num = int(input())

recursive_call(num,4)

print(counter)