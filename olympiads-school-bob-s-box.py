# Problem: Bob's Box (oly21practice82)
# Problem URL: https://dmoj.ca/problem/oly21practice82
# Submission: 4034252 (https://dmoj.ca/submission/4034252)
# Language: Python (PY3)
# Submitted: 2021-11-14T19:50:13+00:00

# Bob's Box

num1,num2,num3 = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

#print((int(num1 / 2)) * num3)
#print((int(num1 / 2) + 1) * num3)

if num1 % 2 == 0:
    print(int(num2 * (num1 / 2) + num3 * (num1 / 2)))
else:
    print(((int(num1 / 2)) * num3) + ((int(num1 / 2) + 1) * num2))