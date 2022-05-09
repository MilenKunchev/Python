my_list = [9, -2, 4, 5, -1, 9, 11, 9]


def find_minimum(l):
    if len(l) == 0:
        raise ValueError('Cannot find the minimum of an empty list.')
    elif len(l) == 1:
        return l[0]
    else:
        min_num = find_minimum(l[1:])
        next_num = l[0]
        if min_num < next_num:
            return min_num
        return next_num


print(find_minimum(my_list))
