# Problem: DWITE '07 R3 #1 - Yet Another Primes Question (dwite07c3p1)
# Problem URL: https://dmoj.ca/problem/dwite07c3p1
# Submission: 3381593 (https://dmoj.ca/submission/3381593)
# Language: Python (PY3)
# Submitted: 2021-02-09T00:05:42+00:00

# DWITE '07 R3 #1 - Yet Another Primes Question

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def factorization(num,prime_list):
    index = 0
    final_list = []
    while True:
        if num % prime_list[index] == 0:
            final_list.append(prime_list[index])
            num = num / prime_list[index]
        else:
            index += 1
        if index >= len(prime_list) - 10:
            return(final_list)

prime_list = get_primes(1000)

num_list = []
for i in range(5):
    num_list.append(int(input()))

for i in range(5):
    temp = factorization(num_list[i], prime_list)
    counter = []
    for i in range(len(temp)):
        if temp[i] not in counter:
            counter.append(temp[i])
    if len(counter) == 3:
        print("valid")
    else:
        print("not")