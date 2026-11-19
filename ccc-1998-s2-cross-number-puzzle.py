# Problem: CCC '98 S2 - Cross Number Puzzle (ccc98s2)
# Problem URL: https://dmoj.ca/problem/ccc98s2
# Submission: 3462356 (https://dmoj.ca/submission/3462356)
# Language: Python (PY3)
# Submitted: 2021-03-02T01:30:36+00:00

# CCC '98 S2 - Cross Number Puzzle

def prefect_number(num):
    factor_list = set()
    for i in range(1,int(num/2) + 1):
        if num % i == 0:
            factor_list.add(i)
            factor_list.add(int(num/i))
    factor_list = sorted(factor_list)
    del factor_list[len(factor_list) - 1]
    if sum(factor_list) == num:
        return True
    else:
        return False

def sum_cubes(num):
    string_num = str(num)
    total_num = 0
    for i in range(len(string_num)):
        total_num += int(string_num[i]) ** 3

    if total_num == num:
        return True
    else:
        return False

numbers = []
numbers1 = []


for i in range(1000,10000):
    if prefect_number(i) == True:
        numbers.append(i)

for i in range(100,1000):
    if sum_cubes(i) == True:
        numbers1.append(i)

print(*numbers)
print(*numbers1)