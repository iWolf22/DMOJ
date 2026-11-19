# Problem: CCC '22 J3 - Harp Tuning (ccc22j3)
# Problem URL: https://dmoj.ca/problem/ccc22j3
# Submission: 4414970 (https://dmoj.ca/submission/4414970)
# Language: Python (PY3)
# Submitted: 2022-03-13T21:07:22+00:00

# CCC '22 J3 - Harp Tuning

string = input()

string_list = []

new_string = ""
num_string = ""
bool_string = "null"
reset = False
for i in range(len(string)):
    if string[i] == "+" or string[i] == "-":
        current_state = "int"
        if string[i] == "+":
            bool_string = "tighten"
        if string[i] == "-":
            bool_string = "loosen"
    elif ord(string[i]) >= 65 and ord(string[i]) <= 90:
        if reset == True:
            reset = False
            string_list.append([new_string,bool_string,num_string])
            new_string = ""
            num_string = ""
            bool_string = "null"
        new_string = new_string + string[i]
    else:
        num_string = num_string + string[i]
        reset = True

if reset == True:
    reset = False
    string_list.append([new_string,bool_string,num_string])
    new_string = ""
    num_string = ""
    bool_string = "null"

for i in range(len(string_list)):
    print(*string_list[i])