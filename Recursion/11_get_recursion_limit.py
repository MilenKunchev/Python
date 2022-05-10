def fetch_recursion_limit():
    try:
        return 1 + fetch_recursion_limit()
    except RuntimeError:
        return 2

print(fetch_recursion_limit())

# https://www.codewars.com/kata/5a1e1b69697598459d000057