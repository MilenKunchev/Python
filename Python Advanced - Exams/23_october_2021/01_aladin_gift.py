from collections import deque
import sys
from io import StringIO

input1 = """105 20 30 25
120 60 11 400 10 1
"""
input2 = """30 5 21 6 0 91
15 9 5 15 8
"""

# sys.stdin = StringIO(input2)

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

crafted_gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()
    present_sum = material + magic_level

    if present_sum < 100 and present_sum % 2 == 0:
        present_sum = (2 * material) + (3 * magic_level)
    elif present_sum < 100 and present_sum % 2 == 1:
        present_sum *= 2
    elif present_sum > 499:
        present_sum /= 2

    if 100 <= present_sum <= 199:
        crafted_gifts['Gemstone'] += 1
    elif 200 <= present_sum <= 299:
        crafted_gifts['Porcelain Sculpture'] += 1
    elif 300 <= present_sum <= 399:
        crafted_gifts['Gold'] += 1
    elif 400 <= present_sum <= 499:
        crafted_gifts['Diamond Jewellery'] += 1
if crafted_gifts['Gemstone'] > 0 and crafted_gifts['Porcelain Sculpture'] > 0 or \
        crafted_gifts['Gold'] > 0 and crafted_gifts['Diamond Jewellery'] > 0:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present, amount in sorted(crafted_gifts.items()):
    if amount > 0:
        print(f'{present}: {amount}')