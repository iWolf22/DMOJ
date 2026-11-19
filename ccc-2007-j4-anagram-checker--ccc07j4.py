# Problem: CCC '07 J4 - Anagram Checker (ccc07j4)
# Problem URL: https://dmoj.ca/problem/ccc07j4
# Submission: 2961560 (https://dmoj.ca/submission/2961560)
# Language: 
# Submitted: 2020-08-20T21:25:10+00:00

def solve():
    phrase1 = input()
    phrase2 = input()
    phrase1 = phrase1.replace(" ","")
    phrase2 = phrase2.replace(" ","")
    phrase1 = phrase1.upper()
    phrase2 = phrase2.upper()
    if len(phrase1) == len(phrase2):
        count1 = 0
        while len(phrase1) > count1:
            temp = 0
            for j in range(len(phrase2)):
                if phrase1[count1] == phrase2[j]:
                    phrase1 = phrase1[:count1] + phrase1[count1 + 1:]
                    phrase2 = phrase2[:j] + phrase2[j + 1:]
                    temp = 1
                    break
            if temp == 0:
                print("Is not an anagram.")
                return
        print("Is an anagram.")
    else:
        print("Is not an anagram.")
solve()