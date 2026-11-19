# Problem: CCC '12 J1 - Speed fines are not fine! (ccc12j1)
# Problem URL: https://dmoj.ca/problem/ccc12j1
# Submission: 4576592 (https://dmoj.ca/submission/4576592)
# Language: Python (PY3)
# Submitted: 2022-05-23T13:59:50+00:00

# CCC '12 J1 - Speed fines are not fine!

limit = int(input())

speed = int(input())

if limit >= speed:
    print("Congratulations, you are within the speed limit!")
elif limit + 20 >= speed:
    print("You are speeding and your fine is $100.")
elif limit + 30 >= speed:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")