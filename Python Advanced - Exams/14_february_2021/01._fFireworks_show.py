from collections import deque
import sys
from io import StringIO

input1 = """5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22

"""

sys.stdin = StringIO(input1)

firework_deque = deque([int(x) for x in input().split(', ')])
explosive_stack = [int(x) for x in input().split(', ')]

fireworks_amounts = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}
fireworks_prepared = False

while True:
    if not firework_deque or not explosive_stack:
        break

    firework = firework_deque[0]
    explosive = explosive_stack[-1]

    if firework <= 0:
        firework_deque.popleft()
        continue
    if explosive <= 0:
        explosive_stack.pop()
        continue

    sum_result = firework + explosive

    if sum_result % 3 == 0 and sum_result % 5 != 0:
        fireworks_amounts['Palm Fireworks'] += 1
        firework_deque.popleft()
        explosive_stack.pop()

    elif sum_result % 5 == 0 and sum_result % 3 != 0:
        fireworks_amounts['Willow Fireworks'] += 1
        firework_deque.popleft()
        explosive_stack.pop()

    elif sum_result % 3 == 0 and sum_result % 5 == 0:
        fireworks_amounts['Crossette Fireworks'] += 1
        firework_deque.popleft()
        explosive_stack.pop()
    else:
        firework -= 1
        firework_deque.popleft()
        firework_deque.append(firework)

    fireworks_prepared = all([v >= 3 for k, v in fireworks_amounts.items()])
    if fireworks_prepared:
        break
if fireworks_prepared:
    print(f'Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_deque:
    print(f'Firework Effects left: {", ".join(str(x) for x in firework_deque)}')
if explosive_stack:
    print(f'Explosive Power left: {", ".join(str(x) for x in explosive_stack)}')
for k, v in fireworks_amounts.items():
    print(f"{k}: {v}")
