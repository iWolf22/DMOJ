# Problem: UCC Coding Competition '21 P3 - Long Pizza (ucc21p3)
# Problem URL: https://dmoj.ca/problem/ucc21p3
# Submission: 4582650 (https://dmoj.ca/submission/4582650)
# Language: Python (PY3)
# Submitted: 2022-05-26T01:43:14+00:00

# UCC Coding Competition '21 P3 - Long Pizza

length_pizza = int(input())

x,y = list(map(int,input().split()))

num_lines = int(input())

cheese_counter = 0

for i in range(num_lines):

    l,r = list(map(int,input().split()))

    if l <= x and r >= y:
        cheese_counter += y - x + 1
    elif l <= x and r >= x:
        cheese_counter += r - x + 1
    elif r >= y and l <= y:
        cheese_counter += y - l + 1
    elif l >= x and r <= y:
        cheese_counter += r - l + 1
    else:
        continue

print(cheese_counter)