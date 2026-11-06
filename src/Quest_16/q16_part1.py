import sys
from typing import List,Tuple
from collections import deque
from functools import lru_cache,cache
import math
from collections import defaultdict
from queue import PriorityQueue

debug = False

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 16, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    if len(sys.argv) >=3:
        debug = True

    df = open(fname, "r")
    orders = [int(x) for x in df.read().splitlines()[0].split(',')]
    if debug:
        print(f"{len(orders)}> {orders}")

    width = 90
    bricks = 0

    for o in orders:
        bricks += math.floor(width/o)
        
    print(f"Total bricks: {bricks}")
