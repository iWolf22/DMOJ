# Problem: CCC '04 J4 - Simple Encryption (ccc04j4)
# Problem URL: https://dmoj.ca/problem/ccc04j4
# Submission: 3690324 (https://dmoj.ca/submission/3690324)
# Language: 
# Submitted: 2021-06-21T16:55:03+00:00

#CCC '04 J4 - Simple Encryption

def shifter(string,num):
    new_string = ""
    for i in range(len(string)):
        temp = num + ord(string[i])
        if temp > 90:
            temp -= 26
        new_string = new_string + chr(temp)
    return new_string

word1 = input()

num_list = []
for i in range(len(word1)):
    num_list.append(ord(word1[i]) - 65)

word3 = input()
word2 = ""

for i in range(len(word3)):
    for j in range(65,90):
        if word3[i] == chr(j):
            word2 = word2 + word3[i]

index = 0

final_word = ""

for i in range(len(word2)):
    
    final_word = final_word + shifter(word2[i],num_list[index])

    index += 1
    if index >= len(num_list):
        index = 0

print(final_word)