# Problem: Least Word (oly21practice93)
# Problem URL: https://dmoj.ca/problem/oly21practice93
# Submission: 4133999 (https://dmoj.ca/submission/4133999)
# Language: Python (PY3)
# Submitted: 2021-12-24T01:23:36+00:00

# Least Word

num_words,num_letters = list(map(int,input().split()))

words_list = []

for i in range(num_words):
    words_list.append(input())

for i in range(len(words_list)):
    for j in range(int(len(words_list[i]) / 2)):
        #print( ord(words_list[i][j]) , ord(words_list[i][-1 * (j + 1)]) )
        #print(words_list[i][j], words_list[i][-1 * (j + 1)])
        if ord(words_list[i][j]) < ord(words_list[i][-1 * (j + 1)]):
            break
        elif ord(words_list[i][j]) > ord(words_list[i][-1 * (j + 1)]):
            words_list[i] = words_list[i][::-1]
            break
        else:
            continue

words_list = sorted(words_list)
words_string = ""

for i in range(len(words_list)):
    words_string = words_string + words_list[i]

print(words_string)