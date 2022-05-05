def generate(index: int, result: list):
    if index >= len(result):
        print(''.join(str(x) for x in result))
    else:
        for i in range(2):
            result[index] = i
            generate(index + 1, result)


""" 
Generates all possible combinations an array with n number of elements.
Elements are 0 and 1 from the loop.
"""
n = 4
ll = [None] * n
generate(0, ll)
