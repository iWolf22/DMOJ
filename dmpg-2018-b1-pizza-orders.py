# Problem: DMPG '18 B1 - Pizza Orders (dmpg18b1)
# Problem URL: https://dmoj.ca/problem/dmpg18b1
# Submission: 3557688 (https://dmoj.ca/submission/3557688)
# Language: Python (PY3)
# Submitted: 2021-04-12T16:15:37+00:00

import math

num1,num2,num3 = list(map(int,input().split()))

print(math.ceil(num1 / 3) + math.ceil(num2 / 3) + math.ceil(num3 / 3))