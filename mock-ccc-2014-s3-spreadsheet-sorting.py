# Problem: Mock CCC '14 S3 - Spreadsheet Sorting (mockccc14s3)
# Problem URL: https://dmoj.ca/problem/mockccc14s3
# Submission: 4753164 (https://dmoj.ca/submission/4753164)
# Language: Python (PY3)
# Submitted: 2022-08-06T23:50:09+00:00

# Mock CCC '14 S3 - Spreadsheet Sorting

rows, cols = list(map(int, input().split()))

matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split())))

instructions = int(input())

for i in range(instructions):
    index = int(input()) - 1
    matrix.sort(key = lambda matrix: matrix[index])

for i in range(len(matrix)):
    print(*matrix[i])