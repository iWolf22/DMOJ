# Problem: Colourful Marbles (oly22practice26)
# Problem URL: https://dmoj.ca/problem/oly22practice26
# Submission: 4478533 (https://dmoj.ca/submission/4478533)
# Language: Python (PY3)
# Submitted: 2022-04-03T23:35:48+00:00

# Colourful Marbles

num_marbles, num_colors = list(map(int,input().split()))

marbles_list = list(map(int,input().split()))

marbles_dic = {i + 1:0 for i in range(num_marbles)}

for i in range(num_marbles):
    marbles_dic[marbles_list[i]] += 1

new_list = []

for i in range(num_marbles):
    if marbles_dic[i + 1] != 0:
        new_list.append(marbles_dic[i + 1])

dif = len(new_list) - num_colors

counter = 0

new_list = sorted(new_list, reverse = False)

for i in range(dif):
    counter += new_list[i]

print(counter)