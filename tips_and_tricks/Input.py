import sys
from io import StringIO

input1 = """3
3
---
-*-
--e
"""

sys.stdin = StringIO(input1)

rows = int(input())
cols = int(input())

lab = []
for _ in range(cols):
    lab.append(list(input()))

print(lab)
