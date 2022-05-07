def solve(a, b):
    # i
    if a == 0 or b == 0:
        return [a, b]
    # ii
    if a >= 2 * b:
        a = a - (2 * b)
        return solve(a, b)
    # iii)
    if b >= 2 * a:
        b = b - (2 * a)
        return solve(a, b)
    else:
        return [a, b]

# https://www.codewars.com/kata/5b752a42b11814b09c00005d
print(solve(6, 19)) #6,7
print(solve(2, 1))  # 0,1
print(solve(22, 5))  # 0,1
print(solve(2, 10))  # 2,2
