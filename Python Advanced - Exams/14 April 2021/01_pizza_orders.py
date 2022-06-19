from collections import deque
import sys
from io import StringIO

input1 = """11, 6, 8, 1
3, 1, 9, 10, 5, 9, 1

"""

# sys.stdin = StringIO(input1)

pizza_orders_deq = deque([int(x) for x in input().split(', ')])
employees_capacities = [int(x) for x in input().split(', ')]

count_pizza_made = 0

while True:
    if pizza_orders_deq and employees_capacities:
        order = pizza_orders_deq.popleft()
    else:
        break
    if order <= 0 or order > 10:
        continue

    if employees_capacities:
        employee = employees_capacities.pop()
    else:
        break
    if order <= employee:
        count_pizza_made += order
        continue
    if order > employee:
        this_order = order
        order -= employee
        while employees_capacities:
            employee = employees_capacities.pop()
            order -= employee
            if order <= 0:
                count_pizza_made += this_order
                break
        if order > 0:
            pizza_orders_deq.appendleft(order)

if not pizza_orders_deq:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {count_pizza_made}')
    if employees_capacities:
        print(f'Employees: {", ".join(str(x) for x in employees_capacities)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in pizza_orders_deq)}')
