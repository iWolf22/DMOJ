# Problem: CCC '07 J2 - I Speak TXTMSG (ccc07j2)
# Problem URL: https://dmoj.ca/problem/ccc07j2
# Submission: 2961234 (https://dmoj.ca/submission/2961234)
# Language: 
# Submitted: 2020-08-20T19:35:16+00:00

list1 = {"CU":"see you",":-)":"I'm happy",":-(":"I'm unhappy",";-)":"wink",":-P":"stick out my tongue","(~.~)":"sleepy","TA":"totally awesome","CCC":"Canadian Computing Competition","CUZ":"because","TY":"thank-you","YW":"you're welcome" ,"TTYL" : "talk to you later"}
list2 = []
word = ""
while word != "TTYL":
    word = input()
    list2.append(word)
for i in range(len(list2)):
    temp = 0
    if list2[i] in list1:
        word1 = list1[list2[i]]
        print(word1)
        temp = 1
    if temp == 0:
        print(list2[i])