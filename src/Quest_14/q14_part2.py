import sys
from typing import List,Tuple
from grid import Grid
from collections import deque


def print_grid(grid:Grid):
    for y in range(grid.y()):
        for x in range(grid.x()):
            state = grid.get(x,y)
            print( f"{"#" if state else "."}", end="" )
        print(' ')
    print(' ')

def count_grid(grid:Grid)->int:
    total = 0
    for y in range(grid.y()):
        for x in range(grid.x()):
            state = grid.get(x,y)
            if state:
                total +=1
    return total

diags = [ (1,1),(-1,-1),(1,-1),(-1,1)]

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
                
def count_grid(grid:Grid)->int:
    total = 0
    for x in range(grid.x()):
        for y in range(grid.y()):
            if grid.get(x,y):
                total += 1
    return total


if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 14, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    
    grid = Grid(max_x=len(lines[0]), max_y=len(lines))
    for y in range(len(lines)):
        r = lines[y]
        if len(r.strip())>0:
            for x in range(len(r)):
                grid.set(x,y, r[x]=='#' )
    print_grid(grid)

    result = 0
    for turn in range(2025):
        ng = round(grid)
        nv = count_grid(ng)
        # print(f"{turn} -> {nv}")
        result += nv
        grid = ng

    print(f"Final result: {result}")
