# Problem: CCC '08 J1 - Body Mass Index (ccc08j1)
# Problem URL: https://dmoj.ca/problem/ccc08j1
# Submission: 3199740 (https://dmoj.ca/submission/3199740)
# Language: Python (PY3)
# Submitted: 2020-12-12T16:33:04+00:00

num1 = float(input())
num2 = float(input())

if num1 / (num2 * num2) > 25:
    print("Overweight")
elif num1 / (num2 * num2) < 18.5:
    print("Underweight")
else:
    print("Normal weight")