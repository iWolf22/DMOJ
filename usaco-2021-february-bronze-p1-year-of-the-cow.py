# Problem: USACO 2021 February Bronze P1 - Year of the Cow (usaco21febb1)
# Problem URL: https://dmoj.ca/problem/usaco21febb1
# Submission: 3483062 (https://dmoj.ca/submission/3483062)
# Language: Python (PY3)
# Submitted: 2021-03-13T14:50:34+00:00

# USACO 2021 February Contest, Bronze

def converter(name1,name2,next,year):
    global year_list
    global names_list
    for i in range(len(year_list)):
        if names_list[name1][1] == year_list[i]:
            counter = i
    total_counter = names_list[name1][0]
    if next == True:
        while True:
            counter += 1
            total_counter += 1
            if counter >= 12:
                counter = 0
            if year_list[counter] == year:
                names_list[name2] = [total_counter,year_list[counter]]
                return
    else:
        while True:
            counter -= 1
            total_counter -= 1
            if counter <= -1:
                counter = 11
            if year_list[counter] == year:
                names_list[name2] = [total_counter,year_list[counter]]
                return 

num1 = int(input())

words_list = []
year_list = ["Ox","Tiger","Rabbit","Dragon","Snake","Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
names_list = {"Bessie":[0,"Ox"]}


for i in range(num1):
    words_list.append(input().split())

word_list = []

for i in range(num1):
    word_list.append([words_list[i][0],words_list[i][3],words_list[i][4],words_list[i][7]])

for i in range(num1):
    for j in range(len(names_list)):
        if list(names_list.keys())[j] == word_list[i][0] and word_list[i][1] == "next":
            converter(word_list[i][0],word_list[i][3],False,word_list[i][2])

        elif list(names_list.keys())[j] == word_list[i][3] and word_list[i][1] == "previous":
            converter(word_list[i][3],word_list[i][0],False,word_list[i][2])

        elif list(names_list.keys())[j] == word_list[i][0] and word_list[i][1] == "previous":
            converter(word_list[i][0],word_list[i][3],True,word_list[i][2])

        elif list(names_list.keys())[j] == word_list[i][3] and word_list[i][1] == "next":
            converter(word_list[i][3],word_list[i][0],True,word_list[i][2])
        else:
            random = 0
            

if names_list["Elsie"][0] < 0:
    print(names_list["Elsie"][0] * -1)
else:
    print(names_list["Elsie"][0])