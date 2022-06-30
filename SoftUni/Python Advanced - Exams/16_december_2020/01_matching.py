from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
successful_matches = 0

while males and females:

    female = females[0]
    male = males[-1]

    if female <= 0:
        females.popleft()
        continue
    if male <= 0:
        males.pop()
        continue
    if male % 25 == 0:
        males.pop()
        if males:
            males.pop()
        continue
    if female % 25 == 0:
        females.pop()
        if females:
            females.pop()
        continue

    if male == female:
        successful_matches += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        males[-1] -= 2

if females:
    females_result = ", ".join(str(x) for x in females)
else:
    females_result = 'none'
if males:
    males_result = ", ".join(str(x) for x in reversed(males))
else:
    males_result = 'none'

print(f'Matches: {successful_matches}')
print(f'Males left: {males_result}')
print(f'Females left: {females_result}')
