from collections import deque


def best_list_pureness(numbers, k):
    nums = deque(numbers)
    pureness_value = float('-inf')
    pureness = 0
    count_rotations = 0
    rotation_number = 0
    for j in range(k + 1):
        for i in range(len(nums)):
            pureness += nums[i] * i
        if pureness > pureness_value:
            pureness_value = pureness
            count_rotations = rotation_number
        # print(f'rotation - {j} puriness = {pureness}')
        pureness = 0
        rotation_number += 1
        last_num = nums.pop()
        nums.appendleft(last_num)

    return f"Best pureness {pureness_value} after {count_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
