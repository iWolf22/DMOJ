# Problem: CCC '06 J1 - Canadian Calorie Counting (ccc06j1)
# Problem URL: https://dmoj.ca/problem/ccc06j1
# Submission: 2960009 (https://dmoj.ca/submission/2960009)
# Language: Python (PY3)
# Submitted: 2020-08-20T03:09:17+00:00

list1 = [461,431,420,0]
list3 = [100,57,70,0]
list2 = [130,160,118,0]
list4 = [167,266,75,0]
l1 = int(input())
l3 = int(input())
l2 = int(input())
l4 = int(input())
print("Your total Calorie count is " + str(list1[l1 - 1] + list2[l2 - 1] + list3[l3 - 1] + list4[l4 - 1]) + ".")