import sys
from typing import List,Tuple
from collections import deque
from functools import lru_cache,cache
import math
from collections import defaultdict
from queue import PriorityQueue
from grid import Grid

debug = False

def print_grid(grid:Grid):
    for y in range(grid.y()):
        for x in range(grid.x()):
            state = grid.get(x,y)
            print( f"{state if state else '.'}", end="" )
        print(' ')
    print(' ')

def solve_grid(grid:Grid, radius: int, volcano: Tuple[int,int]) -> int:
    r2 = radius * radius
    (vx,vy) = volcano
    destroyed = 0
    for y in range(grid.y()):
        for x in range(grid.x()):
            if (vx-x)**2 + (vy-y)**2 <= r2:
                destroyed += grid.get(x,y)
            else:
                grid.set(x,y,0)
    return destroyed

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 17, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    if len(sys.argv) >=3:
        debug = True

    df = open(fname, "r")
    lines = df.read().splitlines()

    volcano = (0,0)

    grid = Grid(max_x=len(lines[0]), max_y=len(lines))
    for y in range(len(lines)):
        r = lines[y]
        if len(r.strip())>0:
            for x in range(len(r)):
                if r[x] == '@':
                    volcano = (x,y)
                    grid.set(x,y,0)
                else:
                    grid.set(x,y,int(r[x]))
    print_grid(grid)
    print(f"Volcano: {volcano}")
    result = solve_grid(grid,10,volcano)

    print_grid(grid)

    print(f"Destroyed: {result}")
