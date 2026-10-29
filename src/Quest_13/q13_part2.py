import sys
from typing import List,Tuple

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 13, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()

    ranges = []
    total = 0
    for l in lines:
        r = [int(x) for x in l.split('-')]
        ranges.append(r)
        total += (r[1]-r[0]) + 1


    wheel = [1] * (total + 1)
    right = 1
    left = -1
    for x in range(len(ranges)):
        (start,end) = ranges[x]
        if x % 2 == 0:
            for y in range(start,end+1):
                wheel[right] = y
                right += 1
        else:
            for y in range(start,end+1):
                wheel[left] = y
                left -=1

    print(f"Wheel: {wheel}")
    pos = 20252025 % len(wheel)

    print(f"Value({pos}): {wheel[pos]}")