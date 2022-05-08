listA = [9, -2, 6, 1, 80, 9, -2]


def find_minimum(l):
    if len(l) == 0:
        raise ValueError('Cannot find the minimum of an empty list.')
    elif len(l) == 1:
        return l[0]
    else:
        current_min_number = find_minimum(l[1:])
        min_num = l[0]
        if current_min_number < min_num:
            min_num = current_min_number
        return min_num


print(find_minimum(listA))
