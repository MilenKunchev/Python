def print_line(space_count, stars_count):
    line_spaces = ''.join([' '] * space_count)
    line_stars = ' '.join(['*'] * stars_count)
    print(line_spaces, line_stars)


def print_rhombus(n):
    for i in range(n):
        spaces = n - 1 - i
        stars = i + 1
        print_line(spaces, stars)

    for i in range(n - 1):
        spaces = i + 1
        stars = n - (i + 1)
        print_line(spaces, stars)


# print_rhombus(3)
print_rhombus(int(input()))
