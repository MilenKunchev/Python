# def numbers_searching(*args):
#     result = []
#     ll = sorted(args)
#     duplicated = set([x for x in ll if ll.count(x) > 1])
#     for i in range(ll[0], ll[-1]+1):
#         if i not in ll:
#             result.append(i)
#     result.append(list(sorted(duplicated)))
#     return result
#
def numbers_searching(*args):
    ll = sorted(args)
    result = []
    duplicated = set()
    for i in range(1, len(ll)):
        if ll[i-1] == ll[i] - 1:
            continue
        if ll[i] == ll[i-1]:
            duplicated.add(ll[i])
            continue
        result.append(ll[i]-1)
    result.append(list(sorted(duplicated)))
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
