def drawing(n):
    if n == 0:
        return

    print(n * "*")
    drawing(n - 1)
    print(n * "*")
    return


drawing(5)
