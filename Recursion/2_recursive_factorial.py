def factorial(num):
    if num == 0:
        return 1
    result = num * factorial(num - 1)
    return result


number = 5
print(f"Factorial {number} is {factorial(number)}")
