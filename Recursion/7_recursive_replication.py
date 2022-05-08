# @countcalls
def replicate(times, number, result=None):
    if result is None:
        result = []
    if times <= 0:
        return []
    else:
        result.append(number)
        replicate(times - 1, number, result)
    return result


# https://www.codewars.com/kata/57547f9182655569ab0008c4/train/python
print(replicate(3, 5))  # [5, 5, 5]
print(replicate(5, 1))  # [1,1,1,1,1]
print(replicate(0, 12))  # []
print(replicate(-1, 12))  # []
print(replicate(8, 0))  # []
