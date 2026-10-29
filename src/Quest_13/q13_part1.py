import sys
from typing import List,Tuple

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 13, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    nums = [int(x) for x in lines]

    wheel = [1] * (len(nums) + 1)
    right = 1
    left = -1
    for x in range(len(nums)):
        if x % 2 == 0:
            wheel[right] = nums[x]
            right += 1
        else:
            wheel[left] = nums[x]
            left -=1

    print(f"Wheel: {wheel}")
    pos = 2025 % len(wheel)

    print(f"Value({pos}): {wheel[pos]}")