from collections import deque
import sys
from io import StringIO

input1 = """Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left

"""
# sys.stdin = StringIO(input1)


def new_position_index(row, col, size, direction):
    if direction == 'up':
        row -= 1
        return row, col

    if direction == 'down':
        row += 1
        return row, col

    if direction == 'left':
        col -= 1
        return row, col

    if direction == 'right':
        col += 1
        return row, col


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


word = input()

size = int(input())
matrix = []
player_row = 0
player_col = 0

for row_index in range(size):
    row = list(input())
    matrix.append(row)
    for col_index in range(size):
        if matrix[row_index][col_index] == 'P':
            player_row = row_index
            player_col = col_index

commands_count = int(input())

for _ in range(commands_count):
    direction_command = input()
    new_row, new_col = new_position_index(player_row, player_col, size, direction_command)
    if is_outside(new_row, new_col, size):
        if word:
            word = word[:-1]
        continue

    matrix[player_row][player_col] = '-'
    player_row, player_col = new_row, new_col

    if matrix[player_row][player_col] != '-':
        word += matrix[player_row][player_col]
        matrix[player_row][player_col] = 'P'
    else:
        matrix[player_row][player_col] = 'P'

print(word)
for r in matrix:
    print(*r, sep='')
