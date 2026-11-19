# Problem: CCC '12 S2 - Aromatic Numbers (ccc12s2)
# Problem URL: https://dmoj.ca/problem/ccc12s2
# Submission: 4576917 (https://dmoj.ca/submission/4576917)
# Language: Python (PY3)
# Submitted: 2022-05-23T16:42:05+00:00

# CCC '12 S2 - Aromatic Numbers

string_list = input().replace(""," ").split()

letter_dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

num_counter = 0

for i in range(int(len(string_list) / 2) - 1):
    if letter_dic[string_list[i * 2 + 1]] < letter_dic[string_list[i * 2 + 3]]:
        num_counter = num_counter - (letter_dic[string_list[i * 2 + 1]] * int(string_list[i * 2]))
    else:
        num_counter = num_counter + (letter_dic[string_list[i * 2 + 1]] * int(string_list[i * 2]))

num_counter = num_counter + (letter_dic[string_list[-1]] * int(string_list[-2]))

print(num_counter)