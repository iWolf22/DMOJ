# Problem: CCC '12 J4 - Big Bang Secrets (ccc12j4)
# Problem URL: https://dmoj.ca/problem/ccc12j4
# Submission: 3427634 (https://dmoj.ca/submission/3427634)
# Language: 
# Submitted: 2021-02-17T03:05:26+00:00

# CCC '12 J4 - Big Bang Secrets

def shifter(string,num):
    new_string = ""
    for i in range(len(string)):
        temp = -num + ord(string[i])
        while temp < 65:
            temp += 26
        while temp > 90:
            temp -= 26
        new_string = new_string + chr(temp)
    return new_string

num = int(input())

word = input()

new_word = ""

for i in range(len(word)):
    new_word = new_word + shifter(word[i],(3 * (i + 1) + num))

print(new_word)