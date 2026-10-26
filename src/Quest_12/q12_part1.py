import sys
from typing import List,Tuple
from grid import Grid
from collections import deque

def print_grid(grid:Grid):
    for y in range(grid.y()):
        for x in range(grid.x()):
            (size,state) = grid.get(x,y)
            print( f"{size}{"*" if state else " "} ", end="" )
        print(' ')
    print(' ')


dirs = [ (0,1),(1,0),(0,-1),(-1,0)]

def process_grid(grid:Grid)->int:
    result = 0
    queue = deque()
    # start with the top left
    queue.append( (0,0) )
    (size,state) = grid.get(0,0)
    grid.set(0,0,(size,True))
    ymax = grid.y() - 1
    xmax = grid.x() - 1
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

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 12, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    
    grid = Grid(max_x=len(lines[0]), max_y=len(lines))
    for y in range(0,len(lines)):
        r = lines[y]
        if len(r.strip())>0:
            for x in range(len(r)):
                grid.set(x,y, (int(r[x]),False) )

    print_grid(grid)    

    result = process_grid(grid)

    print_grid(grid)    
    print(f"Result: {result}")

    print(f"Check: {check_grid(grid)}")
        