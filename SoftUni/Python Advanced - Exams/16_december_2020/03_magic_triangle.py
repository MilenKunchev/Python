def get_magic_triangle(size):
    matrix = [
        [1],
        [1, 1]
    ]

    for row_index in range(2, size):
        row = [1]
        for el_index in range(1, row_index):
            next_element = matrix[row_index - 1][el_index - 1] + matrix[row_index - 1][el_index]
            row.append(next_element)
        row.append(1)
        matrix.append(row)

    return matrix


#
# def get_magic_triangle(size):
#     matrix = [
#         [1], [1, 1]
#     ]
#     col_size = 2
#     for r in range(2, size):
#         row = []
#         prev_row = r - 1
#         col_size += 1
#         for c in range(col_size):
#             first = 0
#             second = 0
#             if c - 1 >= 0:
#                 first = matrix[prev_row][c - 1]
#             if c < col_size - 1:
#                 second = matrix[prev_row][c]
#             element = first + second
#             row.append(element)
#         matrix.append(row)
#
#     return matrix


for r in get_magic_triangle(5):
    print(*r)
