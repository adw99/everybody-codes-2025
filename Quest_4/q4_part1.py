import math
import sys
from typing import List

rot0 = 2025

def solution(lines:List[str]) -> int:
    gears = [int(x) for x in lines if x.strip != '']
    print(f"Gears: {gears}")
    ratio = 1
    prev = -1
    for g in gears:
        if prev != -1:
            ratio = ratio * (prev/g)
        prev = g
    print(f"Total ratio: {ratio}")
    return math.floor(rot0 * ratio)

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 4, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    result = solution( lines )
    print(f"Result: {result}")