# Problem: CCC '13 S2 - Bridge Transport (ccc13s2)
# Problem URL: https://dmoj.ca/problem/ccc13s2
# Submission: 4252258 (https://dmoj.ca/submission/4252258)
# Language: 
# Submitted: 2022-01-26T20:51:58+00:00

# CCC '13 S2 - Bridge Transport

bridge_max = int(input())

num_carts = int(input())

carts_list = []

for i in range(num_carts):
    carts_list.append(int(input()))

carts_list.append(0)
carts_list.append(0)
carts_list.append(0)
carts_list.append(0)

#print(" ")

final = -1

if carts_list[0] > bridge_max:
    final = 0
elif carts_list[0] + carts_list[1] > bridge_max:
    final = 1
elif carts_list[0] + carts_list[1] + carts_list[2] > bridge_max:
    final = 2
else:
    for i in range(num_carts):
        sum_array = carts_list[i] + carts_list[i + 1] + carts_list[i + 2] + carts_list[i + 3]
        #print(sum_array)

        if sum_array > bridge_max:
            if carts_list[i] + carts_list[i + 1] + carts_list[i + 2] <= bridge_max:
                if carts_list[i] + carts_list[i + 1] <= bridge_max:
                    if carts_list[i] <= bridge_max:
                        final = 3 + i
                        break
                    else:
                        final = 2 + i
                        break
                else:
                    final = 1 + i
                    break
            else:    
                final = i
                break

    if final == -1:
        final = num_carts

print(final)