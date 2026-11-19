# Problem: Bob's Lights Game (oly20practice75)
# Problem URL: https://dmoj.ca/problem/oly20practice75
# Submission: 4765190 (https://dmoj.ca/submission/4765190)
# Language: Python (PY3)
# Submitted: 2022-08-11T22:30:38+00:00

# Bob's Lights Game

num_lights, num_switches = list(map(int, input().split()))

lights_list = [0 for i in range(num_lights + 1)]

for i in range(num_switches):
    left, right = list(map(int, input().split()))

    lights_list[left - 1] += 1
    lights_list[right] += 1

for i in range(num_lights):
    lights_list[i + 1] = lights_list[i] + lights_list[i + 1]

counter = 0

for i in range(num_lights):
    if lights_list[i] % 2 == 1:
        counter += 1

print(counter)