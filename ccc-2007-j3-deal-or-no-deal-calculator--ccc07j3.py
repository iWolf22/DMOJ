# Problem: CCC '07 J3 - Deal or No Deal Calculator (ccc07j3)
# Problem URL: https://dmoj.ca/problem/ccc07j3
# Submission: 2961315 (https://dmoj.ca/submission/2961315)
# Language: 
# Submitted: 2020-08-20T20:02:15+00:00

list1 = [100, 500,1000,5000,10000,25000,50000,100000,500000,1000000]
num1 = int(input())
total = 0
totalnum = 10

for i in range(len(list1)):
    total += list1[i]
    
for i in range(num1):
    tempnum = int(input())
    total -= list1[tempnum -1]
    totalnum -= 1

dealnum = int(input())

if dealnum > total / totalnum:
    print("deal")
else:
    print("no deal")