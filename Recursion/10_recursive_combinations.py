def combinations(values: list, index, count, comb: list) :
    if len(comb) == count:
        print(comb)
        return
    for i in range(index, len(values)):
        comb.append(values[i])
        combinations(values, i + 1, count, comb)
        comb.pop()


combinations(list("abc"), 0, 3, [])
