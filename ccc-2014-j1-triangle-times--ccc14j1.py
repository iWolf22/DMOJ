# Problem: CCC '14 J1 - Triangle Times (ccc14j1)
# Problem URL: https://dmoj.ca/problem/ccc14j1
# Submission: 3225134 (https://dmoj.ca/submission/3225134)
# Language: 
# Submitted: 2020-12-20T18:11:43+00:00

#CCC '14 J1 - Triangle Times

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 + num2 + num3 != 180:
    print("Error")
elif num1 == num2 == num3:
    print("Equilateral")
elif num1 == num2 or num1 == num3 or num3 == num2:
    print("Isosceles")
else:
    print("Scalene")