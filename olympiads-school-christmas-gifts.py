# Problem: Christmas Gifts (oly19practice73)
# Problem URL: https://dmoj.ca/problem/oly19practice73
# Submission: 3961483 (https://dmoj.ca/submission/3961483)
# Language: Python (PY3)
# Submitted: 2021-10-17T00:20:25+00:00

# Christmas Gifts

num_prices,money = list(map(int,input().split()))

total_list = []

for i in range(num_prices):
    total_list.append(list(map(int,input().split())))
    total_list[i].append(total_list[i][0] + total_list[i][1])

total_list = sorted(total_list,key=lambda x: float(x[2]))

total_list1 = []
total_list2 = []
counter = 0

for i in range(num_prices):
    counter += total_list[i][2]
    if counter <= money:
        total_list1.append(total_list[i])
    else:
        total_list2.append(total_list[i])

if total_list1 != []:

    total_list1 = sorted(total_list1,key=lambda x: float(x[2]))

    total_list1[len(total_list1) - 1][2] = total_list1[len(total_list1) - 1][2] - int(total_list1[len(total_list1) - 1][0] / 2)

    total_list = total_list1 + total_list2

else:

    total_list = sorted(total_list,key=lambda x: float(x[2]))

    total_list[len(total_list) - 1][2] = total_list[len(total_list) - 1][2] - int(total_list[len(total_list) - 1][0] / 2)

total_list = sorted(total_list,key=lambda x: float(x[2]))

counter = 0

final = 0

for i in range(num_prices):
    counter += total_list[i][2]
    if counter <= money:
        final += 1

#print(total_list)

print(final)