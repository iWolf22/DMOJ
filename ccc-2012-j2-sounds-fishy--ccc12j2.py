# Problem: CCC '12 J2 - Sounds fishy! (ccc12j2)
# Problem URL: https://dmoj.ca/problem/ccc12j2
# Submission: 4576602 (https://dmoj.ca/submission/4576602)
# Language: 
# Submitted: 2022-05-23T14:04:32+00:00

# CCC '12 J2 - Sounds fishy!

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if (num1 == num2 == num3 == num4):
    print("Fish At Constant Depth")
elif (num1 < num2 < num3 < num4):
    print("Fish Rising")
elif (num1 > num2 > num3 > num4):
    print("Fish Diving")
else:
    print("No Fish")