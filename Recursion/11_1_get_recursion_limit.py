import sys


def fetch_recursion_limit():
    def f1(n):
        try:
            return f1(n + 1)
        except RecursionError:
            return n + 3

    return f1(0)


print(fetch_recursion_limit())
""" Returned code error is for run out of time with 5000 -> new solution is needed """

tests = [200, 899, 1000, 89, 567, 390, 768]
for test in tests:
    sys.setrecursionlimit(test)
    print(fetch_recursion_limit())

