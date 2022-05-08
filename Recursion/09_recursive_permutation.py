def permute(index, value):
    if index == len(value):
        print(value)
        return
    for i in range(index, len(value)):
        value[i], value[index] = value[index], value[i]
        permute(index + 1, value)
        value[i], value[index] = value[index], value[i]


print(permute(1, list("abc")))
