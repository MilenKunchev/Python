listA = [9, -2, 6, 1, 80, 9, -2]


def findMinimum(l):
    if len(l) == 0:
        raise ValueError('Cannot find the minimum of an empty list.')
    elif len(l) == 1:
        return l[0]
    else:
        minNumber = findMinimum(l[1:])
        min = l[0]
        if minNumber < min:
            min = minNumber
        return min


findMinimum(listA)

print(findMinimum(listA))
