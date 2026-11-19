# Problem: CCC '10 J2 - Up and Down (ccc10j2)
# Problem URL: https://dmoj.ca/problem/ccc10j2
# Submission: 3165372 (https://dmoj.ca/submission/3165372)
# Language: 
# Submitted: 2020-11-29T17:25:07+00:00

a = int(input())
b = int(input())
c = int(input())
d = int(input())
total = int(input())

nikky = total % (a + b)
if nikky <= a:
    nikky = (int(total / (a + b)) * (a + -b)) + total % (a + b)
else:
    nikky = (int(total / (a + b)) * (a + -b)) + a - (total - (int(total / (a + b)) * (a + -b)) - a)

byron = total % (c + d)
if byron <= c:
    byron = (int(total / (c + d)) * (c + -d)) + total % (c + d)
else:
    byron = (int(total / (c + d)) * (c + -d)) + c - (total - (int(total / (c + d)) * c + -d) - c)

if nikky == byron:
    print("Tied")
elif byron > nikky:
    print("Byron")
else:
    print("Nikky")