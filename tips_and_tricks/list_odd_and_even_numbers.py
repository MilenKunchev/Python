ll = [1, 2, 3, 4]

""" Get EVEN numbers from list"""
ll_even = ll[1::2]
print(ll_even)

ll_even1 = [num for num in ll if num % 2 == 0]
print(ll_even1)

ll_even2 = list(filter(lambda x: (x % 2 != 1), ll))
print(ll_even2)

""" Get ODD numbers from list"""
print(ll[::2])

""" Get sum from ODD numbers"""
print(sum(ll[::2]))
