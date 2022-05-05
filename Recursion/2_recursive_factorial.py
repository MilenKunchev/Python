def factorial(num):
    if num == 0:
        return 1
    result = num * factorial(num - 1)
    return result


print(factorial(5))
