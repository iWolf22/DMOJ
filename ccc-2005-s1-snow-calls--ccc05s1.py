# Problem: CCC '05 S1 - Snow Calls (ccc05s1)
# Problem URL: https://dmoj.ca/problem/ccc05s1
# Submission: 3522192 (https://dmoj.ca/submission/3522192)
# Language: Python (PY3)
# Submitted: 2021-04-01T01:40:21+00:00

string_list = []
num = int(input())

for i in range(num):
    string_list.append(input().replace(""," ").split())

num_list = [str(i) for i in range(10)]

list1 = ["A","B","C"]
list2 = ["D","E","F"]
list3 = ["G","H","I"]
list4 = ["J","K","L"]
list5 = ["M","N","O"]
list6 = ["P","Q","R","S"]
list7 = ["T","U","V"]
list8 = ["W","X","Y","Z"]


for i in range(num):
    new_string = ""
    counter = 0
    temp1 = False
    temp2 = False
    for j in range(len(string_list[i])):
        if string_list[i][j] != "-":
            counter += 1
            if string_list[i][j] in num_list:
                new_string = new_string + string_list[i][j]
            else:
                if string_list[i][j] in list1:
                    new_string = new_string + "2"
                elif string_list[i][j] in list2:
                    new_string = new_string + "3"
                elif string_list[i][j] in list3:
                    new_string = new_string + "4"
                elif string_list[i][j] in list4:
                    new_string = new_string + "5"
                elif string_list[i][j] in list5:
                    new_string = new_string + "6"
                elif string_list[i][j] in list6:
                    new_string = new_string + "7"
                elif string_list[i][j] in list7:
                    new_string = new_string + "8"
                elif string_list[i][j] in list8:
                    new_string = new_string + "9"
                else:
                    print("ERROR")
        if counter == 3 and temp1 == False:
            new_string = new_string + "-"
            temp1 = True
        if counter == 6 and temp2 == False:
            new_string = new_string + "-"
            temp2 = True
        if counter == 10:
            break
        

    print(new_string)