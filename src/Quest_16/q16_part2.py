import sys
from typing import List,Tuple
from collections import deque
from functools import lru_cache,cache
import math
from collections import defaultdict
from queue import PriorityQueue

debug = False



if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 16, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    if len(sys.argv) >=3:
        debug = True

    df = open(fname, "r")
    bricks = [int(x) for x in df.read().splitlines()[0].split(',')]
    if debug:
        print(f"{len(bricks)}> {bricks}")

    spells = []

    for x in range(len(bricks)):
        pos = x+1
        prev_spells = 0
        for s in spells:
            if pos % s == 0:
                prev_spells += 1
        if bricks[x] > prev_spells:
            spells.append(pos)

    print(f"Spells> {spells}")

    result = 1
    for x in spells:
        result *= x
        
    print(f"Result: {result}")
