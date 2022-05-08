# f(n) = f(n-1) * n
# f(1) = 1
# f(0) = 0
def factorial(n):
    print(f"Calculating f({n})")
    if n == 0 or n == 1:
        return 1
    result = n * factorial(n - 1)
    print(f"f({n})={result}")
    return result


number = 5

factorial(number)
