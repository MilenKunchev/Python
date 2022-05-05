def calc_sum(arr, index):
    if index == len(arr):
        return 0
    result = arr[index] + calc_sum(arr, index + 1)
    return result


arr = [1, 2, 3, 4, 5]
print(calc_sum(arr, 0))
