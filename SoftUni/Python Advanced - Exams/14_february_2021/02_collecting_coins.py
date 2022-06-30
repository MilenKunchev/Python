import sys
from io import StringIO

input1 = """5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right
"""
input2 = """8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
down
up
left

"""

sys.stdin = StringIO(input2)


def read_matrix():
    for row_index in range(n):
        row_data = input().split()
        locate_player_position(row_data, row_index)
        matrix.append(row_data)


def locate_player_position(row_data, row_index):
    if 'P' in row_data:
        player_position.append([row_index, row_data.index('P')])


def move_up(ma, row, col):
    return row - 1, col


def move_down(ma, row, col):
    return row + 1, col


def move_left(ma, row, col):
    return row, col - 1


def move_right(ma, row, col):
    return row, col + 1


def is_outside(ma, row, col):
    return row < 0 or col < 0 or row >= len(ma) or col >= len(ma[0])


def traverse_field(ma, row, col):
    rows = len(ma)
    cols = len(ma[0])
    if row < 0:
        row = rows - 1

    if row > rows - 1:
        row = 0

    if col < 0:
        col = cols - 1

    if col > cols - 1:
        col = 0

    return row, col


def game_over(coins):
    coins = coins // 2
    print(f"Game over! You've collected {coins} coins.")


def you_win(coins):
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        return True


n = int(input())

matrix = []
player_position = []
coins = 0
moves = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right,

}

read_matrix()
player_row, player_col = player_position[0]

while True:
    command = input()
    new_row, new_col = moves[command](matrix, player_row, player_col)

    if is_outside(matrix, new_row, new_col):
        new_row, new_col = traverse_field(matrix, new_row, new_col)

    matrix[player_row][player_col] = '0'
    player_row, player_col = new_row, new_col
    player_position.append([player_row, player_col])

    position_on_matrix = eval('matrix[player_row][player_col]')
    if position_on_matrix.isdigit():
        coins += int(position_on_matrix)
        if you_win(coins):
            break
        position_on_matrix = '0'
        continue
    game_over(coins)
    break
print('Your path:')
[print(step) for step in player_position]
