import math
import sys
from typing import List

rot0 = 100

def solution(lines:List[str]) -> int:
    gears = []
    for l in lines:
        if '|' in l:
            gears.append([int(x) for x in l.split('|')])
        else:
            gears.append(int(l))

    print(f"Gears: {gears}")
    ratio = 1
    prev = -1
    for g in gears:
        if prev != -1:
            if isinstance(g,list):
                ratio = ratio * (prev/g[0])
                prev = g[1]
            else:
                ratio = ratio * (prev/g)
                prev = g
        else:
            prev = g[0] if isinstance(g,list) else g
    print(f"Total ratio : {ratio}")
    return math.floor(rot0 * ratio)

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 4, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    result = solution( lines )
    print(f"Result: {result}")