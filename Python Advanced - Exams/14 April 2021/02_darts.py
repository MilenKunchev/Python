import sys
from io import StringIO

input1 = """George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)
"""

# sys.stdin = StringIO(input1)

first_player, second_player = input().split(', ')

size = 7
matrix = []

players_data = {
    0: [501, 0],
    1: [501, 0]
}
players_names = [first_player, second_player]
result = 0
turn = -1

for _ in range(size):
    r = input().split()
    matrix.append(r)


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


while True:
    turn += 1
    player = turn % 2
    players_data[player][1] += 1

    row, col = (int(x) for x in input().strip('()').split(', '))

    if is_outside(row, col, size):
        continue
    # points collecting
    hit_result = matrix[row][col]
    if hit_result == 'B':
        name = players_names[player]
        count_turns = players_data[player][1]
        print(f"{name} won the game with {count_turns} throws!")
        break

    elif hit_result.isnumeric():
        result += int(hit_result)
        players_data[player][0] -= result

    elif hit_result == 'D':
        r_num = int(matrix[row][6])
        l_num = int(matrix[row][0])
        u_num = int(matrix[0][col])
        d_num = int(matrix[6][col])
        result = 2 * (sum([r_num, l_num, d_num, u_num]))
        players_data[player][0] -= result

    elif hit_result == 'T':
        r_num = int(matrix[row][6])
        l_num = int(matrix[row][0])
        u_num = int(matrix[0][col])
        d_num = int(matrix[6][col])
        result = 3 * (sum([r_num, l_num, d_num, u_num]))
        players_data[player][0] -= result

    result = 0
    if players_data[player][0] <= 0:
        name = players_names[player]
        count_turns = players_data[player][1]
        print(f"{name} won the game with {count_turns} throws!")
        break
# name = players_names[player]
# count_turns = players_data[player][1]
# print(f'{name} {count_turns} throw: {players_data[player][0]}')
# print()
