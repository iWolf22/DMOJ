# Problem: CCC '13 J2 - Rotating letters (ccc13j2)
# Problem URL: https://dmoj.ca/problem/ccc13j2
# Submission: 3223134 (https://dmoj.ca/submission/3223134)
# Language: Python (PY3)
# Submitted: 2020-12-20T00:35:50+00:00

#CCC '13 J2 - Rotating letters

word = input()

list_letters = ["I","O","S","H","Z","X","N"]

final_bool = False

for i in range(len(word)):
    temp_bool = False
    for j in range(len(list_letters)):
        if list_letters[j] == word[i]:
            temp_bool = True
    if temp_bool == False:
        final_bool = True

if final_bool == False:
    print("YES")
else:
    print("NO")