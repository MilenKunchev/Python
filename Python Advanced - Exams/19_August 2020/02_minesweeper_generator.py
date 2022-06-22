import sys
from io import StringIO


def is_outside(row, col, rows, cols):  # check if indexes are outside the matrix
    return row < 0 or col < 0 or row >= rows or col >= cols


def get_matrix_element_up(matrix, my_row, my_col):
    new_row = my_row - 1
    new_col = col
    if new_row < 0:
        return None
    return matrix[new_row][new_col]


def get_matrix_element_right(matrix, my_row, my_col):
    new_row = my_row
    new_col = col + 1
    if new_col >= len(matrix[new_row]):
        return None
    return matrix[new_row][new_col]


def get_matrix_element_down(matrix, my_row, my_col):
    new_row = my_row + 1
    new_col = col
    if new_row >= len(matrix):
        return None
    return matrix[new_row][new_col]


def get_matrix_element_left(matrix, my_row, my_col):
    new_row = my_row
    new_col = my_col - 1
    if new_col < 0:
        return None
    return matrix[new_row][new_col]


def get_matrix_element_right_up_diagonal(matrix, my_row, my_col):
    new_row = my_row - 1
    new_col = my_col + 1
    if is_outside(new_row, new_col, len(matrix), len(matrix[0])):
        return None
    return matrix[new_row][new_col]


def get_matrix_element_right_down_diagonal(matrix, my_row, my_col):
    new_row = my_row + 1
    new_col = my_col + 1
    if is_outside(new_row, new_col, len(matrix), len(matrix[0])):
        return None
    return matrix[new_row][new_col]


def get_matrix_element_left_down_diagonal(matrix, my_row, my_col):
    new_row = my_row + 1
    new_col = my_col - 1
    if is_outside(new_row, new_col, len(matrix), len(matrix[0])):
        return None
    return matrix[new_row][new_col]


def get_matrix_element_left_up_diagonal(matrix, my_row, my_col):
    new_row = my_row - 1
    new_col = my_col - 1
    if is_outside(new_row, new_col, len(matrix), len(matrix[0])):
        return None
    return matrix[new_row][new_col]


input1 = """5
3
(1, 1)
(2, 4)
(4, 1)

"""
# sys.stdin = StringIO(input1)

size = int(input())
bombs_count = int(input())
field_matrix = [[0 for c in range(size)] for r in range(size)]

for _ in range(bombs_count):
    bomb_row, bomb_col = (int(x) for x in input().strip('()').split(', '))
    field_matrix[bomb_row][bomb_col] = "*"

bombs_near_cell_count = 0

for row in range(size):
    for col in range(size):
        if field_matrix[row][col] == '*':
            continue
        if get_matrix_element_up(field_matrix, row, col) == '*':
            bombs_near_cell_count += 1
        if get_matrix_element_right(field_matrix, row, col) == '*':
            bombs_near_cell_count += 1
        if get_matrix_element_down(field_matrix, row, col) == '*':
            bombs_near_cell_count += 1
        if get_matrix_element_left(field_matrix, row, col) == '*':
            bombs_near_cell_count += 1
        if get_matrix_element_right_up_diagonal(field_matrix, row, col) == '*':
            bombs_near_cell_count += 1
        if get_matrix_element_right_down_diagonal(field_matrix, row, col) == '*':
            bombs_near_cell_count += 1
        if get_matrix_element_left_down_diagonal(field_matrix, row, col) == '*':
            bombs_near_cell_count += 1
        if get_matrix_element_left_up_diagonal(field_matrix, row, col) == '*':
            bombs_near_cell_count += 1

        field_matrix[row][col] = bombs_near_cell_count
        bombs_near_cell_count = 0

for r in field_matrix:
    print(*r)
