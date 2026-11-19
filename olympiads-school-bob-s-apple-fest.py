# Problem: Bob's Apple Fest (oly21practice56)
# Problem URL: https://dmoj.ca/problem/oly21practice56
# Submission: 3687191 (https://dmoj.ca/submission/3687191)
# Language: Python (PY3)
# Submitted: 2021-06-19T22:03:55+00:00

# Bob's Apple Fest

num1,num2 = list(map(int,input().split()))

counter = max(num1,num2)
num3 = min(num1,num2)
num4 = max(num1,num2)

while True:
    if counter % num3 == 0:
        break
    else:
        counter += num4

print(counter)