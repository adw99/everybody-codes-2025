import sys
from typing import List,Tuple
from grid import Grid
from collections import deque
import math

debug = False

def print_grid(grid:Grid):
    for y in range(grid.y()):
        for x in range(grid.x()):
            (size,state) = grid.get(x,y)
            print( f"{size}{"*" if state else " "} ", end="" )
        print(' ')
    print(' ')

def print_grid2(grid:Grid):
    for y in range(grid.y()):
        for x in range(grid.x()):
            (size,state) = grid.get(x,y)
            print( f"{"*" if state else " "}", end="" )
        print(' ')
    print(' ')


dirs = [ (0,1),(1,0),(0,-1),(-1,0)]

def process_grid(grid:Grid, start:List[Tuple[int,int]])->int:
    result = 0
    ymax = grid.y() - 1
    xmax = grid.x() - 1
    queue = deque()
    for s in start:
        (sx,sy) = s
        queue.append( s )
        (size,_) = grid.get(sx,sy)
        grid.set(sx,sy,(size,True))
    while len(queue)>0:
        (x,y) = queue.popleft()
        (size,_) = grid.get(x,y)
        grid.set(x,y,(size,True))
        result += 1

        for dx,dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= xmax and 0<= ny <= ymax:
                (nsize,nstate) = grid.get(nx,ny)
                if nsize <= size and not nstate:
                    grid.set(nx,ny,(nsize,True))
                    queue.append( (nx,ny))
            
    return result

def check_grid(grid:Grid)->int:
    count = 0
    for y in range(grid.y()):
        for x in range(grid.x()):
            (_,state) = grid.get(x,y)
            if state:
                count += 1

    return count

def grid_set(grid:Grid):
    result = set()
    for x in range(grid.x()):
        for y in range(grid.y()):
            (_,state) = grid.get(x,y)
            if state:
                result.add( (x,y) )
    return result


def solve(grid: Grid):
    top3 = []
    needed = 3
    while len(top3)<needed:        
        results = []
        g2 = grid.copy()
        if len(top3)> 0:
            process_grid(g2, top3)
        for x in range(grid.x()):
            for y in range(grid.y()):
                if( (x,y) not in top3):
                    g = g2.copy()

                    start = [(x,y)]
                    c = process_grid(g,start)
                    results.append( (x,y,c))
        results = sorted(results, key=lambda x:x[2], reverse=True)
        (x,y,score) = results[0]
        print(f">>> {x},{y} -> {score}")
        top3.append((x,y))

    # Reprocess with top 3 together
    result = process_grid(grid,top3)
    return result


if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 12, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    debug = True if len(sys.argv) >=3 else False
    df = open(fname, "r")
    lines = df.read().splitlines()
    
    grid = Grid(max_x=len(lines[0]), max_y=len(lines))
    for y in range(0,len(lines)):
        r = lines[y]
        if len(r.strip())>0:
            for x in range(len(r)):
                grid.set(x,y, (int(r[x]),False) )

    if debug:
        print_grid(grid)    

    print(f"Grid is {grid.x()} x {grid.y()}")
    result = solve(grid)

    print_grid2(grid)    

    print(f"Result: {result}")

    print(f"Check: {check_grid(grid)}")
        