""" While loop """
print("while loop")
n = 5
index = 1
while True:
    print(index)
    if index == n:
        break
    index += 1

""" Recursion """
print("recursion")


def nums(n):
    if n == 6:
        return
    print(n)
    nums(n + 1)
    # print(n)


nums(1)
