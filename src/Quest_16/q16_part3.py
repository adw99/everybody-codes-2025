import sys
from typing import List,Tuple
from collections import deque
from functools import lru_cache,cache
import math
from collections import defaultdict
from queue import PriorityQueue

debug = False

# This 'should' solve the problem, but seems to come up slightly low, I think due to numeric precision issues with large numbers (?)
def solve_lcm(spells:List[int], bricks:int) -> int:
    result = 0
    pos = 1

    lcm = math.lcm(*spells)
    print(f"LCM> {lcm}")

    product = sum([ lcm/x for x in spells])

    print(f"product> {product}")

    length = bricks * (lcm/product) 

    return length


def calc_bricks(spells,rows):
    bricks = 0
    for s in spells:
        bricks += math.floor( rows/s )
    return bricks

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 16, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    if len(sys.argv) >=3:
        debug = True

    df = open(fname, "r")
    columns = [int(x) for x in df.read().splitlines()[0].split(',')]
    if debug:
        print(f"{len(columns)}> {columns}")


    spells = []

    for x in range(len(columns)):
        pos = x+1
        prev_spells = 0
        for s in spells:
            if pos % s == 0:
                prev_spells += 1
        if columns[x] > prev_spells:
            spells.append(pos)
        if columns[x] > (prev_spells+1):
            print(f"WARN> {columns[x]} vs {prev_spells+1}")

    print(f"Spells> {spells}")

    bricks = 202520252025000

    length1 = math.floor(solve_lcm(spells,bricks))

    print(f"LCM Result: {length1}")

    lb = 0
    wl = length1
    last_wl = wl
    while lb < bricks:
        lb = calc_bricks(spells,wl)
        print(f"Bricks> {lb} vs {bricks} : {wl}")
        if bricks == lb:
            last_wl = wl
        else:
            last_wl = wl - 1
        wl += 1
    solution = last_wl - 1
    print(f"Solution:  {last_wl}")