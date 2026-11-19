# Problem: ECOO '20 P2 - Online Shopping (ecoo20p2)
# Problem URL: https://dmoj.ca/problem/ecoo20p2
# Submission: 3945893 (https://dmoj.ca/submission/3945893)
# Language: Python (PY3)
# Submitted: 2021-10-10T23:13:43+00:00

test_cases = int(input())

for i in range(test_cases):

    num_stores = int(input())
    product_list = []
    product_dic = {}

    for j in range(num_stores):
        num_products = int(input())

        for a in range(num_products):
            
            temp = input().split()
            
            if temp[0] in product_list:
                product_dic[temp[0]].append([int(temp[1]),int(temp[2])])
            else:
                product_list.append(temp[0])
                product_dic[temp[0]] = [[int(temp[1]),int(temp[2])]]

    for j in range(len(product_list)):
        product_dic[product_list[j]].sort(key=lambda x: x[0])

    counter = 0
    num_items = int(input())
    for j in range(num_items):
        item_name,item_amount = input().split()
        item_amount = int(item_amount)
        for a in range(len(product_dic[item_name])):
            if item_amount > product_dic[item_name][a][1]:
                counter += product_dic[item_name][a][0] * product_dic[item_name][a][1]
                item_amount -= product_dic[item_name][a][1]
            else:
                counter += product_dic[item_name][a][0] * item_amount
                break
        
    print(counter)