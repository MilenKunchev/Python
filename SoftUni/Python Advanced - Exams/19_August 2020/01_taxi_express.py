# list of customers with numbers represents time to drive
# list of taxis represent how much time can drive before refill
# keep total time for all customers
# first customer in them last taxi

from collections import deque
import sys
from io import StringIO

input1 = """4, 6, 8, 5, 1
1, 9, 15, 10, 6

"""
# sys.stdin = StringIO(input1)

customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]

total_time = 0

while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis.pop()

    if current_customer > current_taxi:
        continue

    customers.popleft()
    total_time += current_customer

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(x) for x in customers)}')