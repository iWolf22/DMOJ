# Problem: DMOPC '18 Contest 6 P1 - DNA or RNA? (dmopc18c6p1)
# Problem URL: https://dmoj.ca/problem/dmopc18c6p1
# Submission: 3294412 (https://dmoj.ca/submission/3294412)
# Language: Python (PY3)
# Submitted: 2021-01-16T16:22:25+00:00

# DMOPC '18 Contest 6 P1 - DNA or RNA?

num1 = int(input())
word = input()
temp_bool = False

dic = [False,False,False,False,False]
dic1 = ["A","C","G","T","U"]

for i in range(len(word)):
    for j in range(5):
        if dic1[j] == word[i]:
            dic[j] = True

for i in range(len(word)):
    if word[i] not in dic1:
        temp_bool = True
        

if dic[0] == True and dic[1] == True and dic[2] == True and dic[3] == True and dic[4] == True:
    print("neither")
elif dic[3] == True and dic[4] == True:
    print("neither")
elif dic[0] == True and dic[1] == True and dic[2] == True and dic[3] == True and temp_bool == False:
    print("DNA")
elif dic[0] == True and dic[1] == True and dic[2] == True and dic[4] == True and temp_bool == False:
    print("RNA")
elif temp_bool == False and (dic[0] == True or dic[1] == True or dic[2] == True):
    print("both")
elif dic[3] == True and temp_bool == False:
    print("DNA")
elif dic[4] == True and temp_bool == False:
    print("RNA")
else:
    print("neither")