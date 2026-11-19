# Problem: Flip the Switches (fts)
# Problem URL: https://dmoj.ca/problem/fts
# Submission: 3472327 (https://dmoj.ca/submission/3472327)
# Language: Python (PY3)
# Submitted: 2021-03-07T16:42:53+00:00

# Flip the Switches

num = int(input())

switches = input()

switches_list = []

for i in range(len(switches)):
    switches_list.append(switches[i])

if switches_list[0] == "1":
    counter = 1
else:
    counter = 0

pre_switch = switches_list[0]
if len(switches_list) > 1:
    switch = switches_list[1]

    if pre_switch == "0" and switch == "1":
        counter += 2

for i in range(1,len(switches_list)):
    pre_switch = switch
    switch = switches_list[i]
    if pre_switch == "0" and switch == "1":
        counter += 2

print(counter)