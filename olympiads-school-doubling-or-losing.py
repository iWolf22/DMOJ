# Problem: Doubling or Losing (oly21practice87)
# Problem URL: https://dmoj.ca/problem/oly21practice87
# Submission: 4126017 (https://dmoj.ca/submission/4126017)
# Language: Python (PY3)
# Submitted: 2021-12-21T02:48:07+00:00

# Doubling or Losing

temp_num = input()
num = str(int(temp_num) *2)

new_num = ""

#print(temp_num,new_num,num)

for i in range(len(num) - 1):
    new_num = new_num + str(num[i])

print(int(temp_num) - int(new_num))