# Problem: CCC '10 J3 - Punchy (ccc10j3)
# Problem URL: https://dmoj.ca/problem/ccc10j3
# Submission: 3130909 (https://dmoj.ca/submission/3130909)
# Language: 
# Submitted: 2020-11-13T23:02:06+00:00

#Solve 2010j3 using exec. (There will be a solution provided for this)

total_list = []
stop = False

while stop == False:
    temp_list = input().split()
    total_list.append(temp_list)
    if temp_list[0] == "7":
        stop = True

var_a = 0
var_b = 0

math_dic = {
    "3":"+",
    "4":"*",
    "5":"-",
    "6":"/"
}

stop = False
while stop == False:
    for i in range(len(total_list)):
        if total_list[i][0] == "7":
            stop = True
        elif total_list[i][0] == "1":
            if total_list[i][1] == "A":
                var_a = int(total_list[i][2])
            else:
                var_b = int(total_list[i][2])
        elif total_list[i][0] == "2":
            if total_list[i][1] == "A":
                print(var_a)
            else:
                print(var_b)
        elif total_list[i][0] == "3" or total_list[i][0] == "4" or total_list[i][0] == "5" or total_list[i][0] == "6":
            letter_dic = {
                "A":var_a,
                "B":var_b
            }
            string = str(letter_dic[total_list[i][1]]) + str(math_dic[total_list[i][0]]) + str(letter_dic[total_list[i][2]])
            if total_list[i][1] == "A":
                var_a = eval(string)
                var_a = int(var_a)
            else:
                var_b = eval(string)
                var_b = int(var_b)
        else:
            print("Error 404")

#Bad Hard Coding

        # elif total_list[i][0] == "3":
        #     if total_list[i][1] == "A":
        #         var_a = var_a + var_b
        #     else:
        #         var_b = var_a + var_b
        # elif total_list[i][0] == "4":
        #     if total_list[i][1] == "A":
        #         var_a = var_a * var_b
        #     else:
        #         var_b = var_a * var_b
        # elif total_list[i][0] == "5":
        #     if total_list[i][1] == "A":
        #         var_a = var_a - var_b
        #     else:
        #         var_b = var_b - var_a
        # elif total_list[i][0] == "6":
        #     if total_list[i][0] == "A":
        #         var_a = var_a / var_b
        #     else:
        #         var_b = var_b / var_a