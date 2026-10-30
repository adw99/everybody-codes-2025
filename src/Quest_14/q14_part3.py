import sys
from typing import List,Tuple
from grid import Grid
from collections import deque
from functools import lru_cache,cache

def print_grid(grid:Grid):
    for y in range(grid.y()):
        for x in range(grid.x()):
            state = grid.get(x,y)
            print( f"{"#" if state else "."}", end="" )
        print(' ')
    print(' ')


diags = [ (1,1),(-1,-1),(1,-1),(-1,1)]

@cache
def round(grid:Grid) -> Grid:
    ng = Grid(max_x=grid.x(),max_y=grid.y())
    xmax = grid.x() - 1
    ymax = grid.y() - 1

    for x in range(grid.x()):
        for y in range(grid.y()):
            state = grid.get(x,y)
            count = 0
            for (dx,dy) in diags:
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= xmax and 0 <= ny <= ymax:
                    if grid.get(nx,ny):
                        count += 1
            new_state = False
            if state:
                new_state = (count % 2 == 1)
            else:
                new_state = (count % 2 == 0)
            ng.set(x,y,new_state)

    return ng
                
@cache
def count_grid(grid:Grid)->int:
    total = 0
    for y in range(grid.y()):
        for x in range(grid.x()):
            state = grid.get(x,y)
            if state:
                total +=1
    return total

@cache
def compare_grid_subset(ref_grid: Grid, grid: Grid)->bool:
    off_x = int( ( grid.x() - ref_grid.x() ) / 2 )
    off_y = int( ( grid.y() - ref_grid.y() ) / 2 )

    for x in range(ref_grid.x()):
        for y in range(ref_grid.y()):
            if ref_grid.get(x,y) != grid.get(off_x + x,off_y + y):
                return False
    return True

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 14, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    
    grid = Grid(max_x=len(lines[0]), max_y=len(lines))
    for y in range(len(lines)):
        r = lines[y]
        if len(r.strip())>0:
            for x in range(len(r)):
                grid.set(x,y, r[x]=='#' )
    print(f"Grid is {grid.x()} by {grid.y()}")
    print_grid(grid)
    ref_grid = grid

    size=34
    grid = Grid(max_x=34,max_y=34)
    for x in range(size):
        for y in range(size):
            grid.set(x,y,False)


    result = 0

    for turn in range(1000000000):
        ng = round(grid)
        match = compare_grid_subset(ref_grid, ng)
        if match:
            # print(f"Match: {turn}")
            nv = count_grid(ng)
            result += nv
        grid = ng


    print(f"Final result: {result}")
