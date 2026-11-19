# Problem: CCC '14 S2 - Assigning Partners (ccc14s2)
# Problem URL: https://dmoj.ca/problem/ccc14s2
# Submission: 3434173 (https://dmoj.ca/submission/3434173)
# Language: 
# Submitted: 2021-02-19T02:41:26+00:00

#CCC '14 S2 - Assigning Partners

def swap(name_list1,name_list2):
    
    name_list = []

    for i in range(len(name_list1)):
        name_list.append([name_list1[i],name_list2[i]])
        if name_list1[i] == name_list2[i]:
            return False
    
    for i in range(len(name_list)):
        for j in range(len(name_list)):
            if (name_list[i][0] != name_list[j][0] and name_list[i][1] == name_list[j][1]) or (name_list[i][1] != name_list[j][0] and name_list[i][0] == name_list[j][1]):
                return False

    return True

num1 = int(input())

name_list1 = input().split()
name_list2 = input().split()

if swap(name_list1,name_list2) == True:
    print("good")
else:
    print("bad")