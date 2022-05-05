def calc_sum(arr, index):
    if index == len(arr):
        return 0
    print(f" Before recursion index = {index}")
    result = arr[index] + calc_sum(arr, index + 1)
    print(f" After recursion index = {index} Number = {arr[index]} Result = {result}")
    return result


arr = [3, 4, 5]
print(calc_sum(arr, 0))
