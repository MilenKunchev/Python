import sys
from io import StringIO

input1 = """10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)

"""
input2 = """B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)

"""

# sys.stdin = StringIO(input2)

size = 6
matrix = []
points = 0
for _ in range(size):
    r = input().split()
    matrix.append(r)

for _ in range(3):
    row, col = (int(x) for x in input().strip('()').split(', '))
    if row < 0 or col < 0 or row >= size or col >= size:
        continue

    if matrix[row][col] == 'B':
        matrix[row][col] = '0'
        for r in range(size):
            for c in range(size):
                if c == col:
                    points += int(matrix[r][c])

if points <100:
    print(f'Sorry! You need {100-points} points more to win a prize.')
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")


