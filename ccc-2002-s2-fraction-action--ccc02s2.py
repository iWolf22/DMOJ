# Problem: CCC '02 S2 - Fraction Action (ccc02s2)
# Problem URL: https://dmoj.ca/problem/ccc02s2
# Submission: 4568640 (https://dmoj.ca/submission/4568640)
# Language: 
# Submitted: 2022-05-19T01:54:38+00:00

# CCC '02 S2 - Fraction Action

num1 = int(input())
num2 = int(input())
if (num1 == 0):
    print(0)
elif (num1 % num2 == 0):
    print(int(num1 / num2))
else:

    num_first = int(num1 / num2)

    num_top = (num1 % num2) / num2
    num_bottom = 1

    counter = 1

    while (round(num_top * counter,8) % 1 != 0 or round(num_bottom * counter,8) % 1 != 0):
        counter += 1
        
    if num_first != 0:
        print(str(int(num_first)) + " " + str(int((round(num_top * counter, 8)))) + "/" + str(int((round(num_bottom * counter, 8)))))
    else:
        print(str(int((round(num_top * counter, 8)))) + "/" + str(int((round(num_bottom * counter, 8)))))