# Problem: USACO 2021 January Bronze P3 - Just Stalling (usaco21janb3)
# Problem URL: https://dmoj.ca/problem/usaco21janb3
# Submission: 3960524 (https://dmoj.ca/submission/3960524)
# Language: Python (PY3)
# Submitted: 2021-10-16T18:21:34+00:00

# USACO 2021 January Bronze P3 - Just Stalling

num = int(input())

cow_list = list(map(int, input().split()))
stall_list = list(map(int, input().split()))

cow_list.sort(reverse=True)
stall_list.sort(reverse=True)

counter = 1

for i in range(num):
    temp = 0
    for j in range(i,num):
        if cow_list[i] <= stall_list[j]:
            temp += 1
    counter *= temp

print(counter)