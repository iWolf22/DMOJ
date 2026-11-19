# Problem: CCC '04 S3 - Spreadsheet (ccc04s3)
# Problem URL: https://dmoj.ca/problem/ccc04s3
# Submission: 4794088 (https://dmoj.ca/submission/4794088)
# Language: Python (PY3)
# Submitted: 2022-08-24T01:45:39+00:00

# CCC '04 S3 - Spreadsheet

visted_array = [[0 for i in range(9)] for j in range(10)]

def recursive_builder(x_loc, y_loc):
    global sheet1
    global sheet2
    global visted_array

    if (sheet1[x_loc][y_loc] == "null"):
        sheet1[x_loc][y_loc] = "null"
        return "null"

    if (visted_array[x_loc][y_loc] == 1):
        sheet1[x_loc][y_loc] = "null"
        return "null"

    if (sheet2[x_loc][y_loc] == 1):
        return sheet1[x_loc][y_loc]
    else:
        sum_counter = 0
        for i in range(len(sheet1[x_loc][y_loc])):
            visted_array[x_loc][y_loc] = 1
            returned_value = recursive_builder(sheet1[x_loc][y_loc][i][0], sheet1[x_loc][y_loc][i][1])
            if (returned_value == "null"):
                sheet1[x_loc][y_loc] = "null"
                return "null"
            else:
                sum_counter += returned_value
        sheet1[x_loc][y_loc] = sum_counter
        sheet2[x_loc][y_loc] = 1
        visted_array[x_loc][y_loc] = 0
        return sum_counter

sheet1 = [[] for i in range(10)]
sheet2 = [[0 for i in range(9)] for j in range(10)]

for i in range(10):
    user_input = input().split()
    for j in range(len(user_input)):
        int_input = True
        for a in range(len(user_input[j])):
            if 48 > ord(user_input[j][a]) or 57 < ord(user_input[j][a]):
                int_input = False

        if int_input == True:
            sheet1[i].append(int(user_input[j]))
            sheet2[i][j] = 1
        else:
            sheet1[i].append([])
            for a in range(int((len(user_input[j]) + 1) / 3)):
                sheet1[i][j].append([int(ord(user_input[j][a * 3]) - 65), int(user_input[j][a * 3 + 1]) - 1])

for i in range(len(sheet2)):
    for j in range(len(sheet2[i])):
        if sheet2[i][j] == 0:
            visted_array = [[0 for i in range(9)] for j in range(10)]
            sheet1[i][j] = recursive_builder(i, j)
            if (sheet1[i][j] != "null"):
                sheet2[i][j] = 1
            

for i in range(len(sheet1)):
    for j in range(len(sheet1[i])):
        if (sheet1[i][j] == "null"):
            print("*", end = " ")
        else:
            print(sheet1[i][j], end = " ")
    print()