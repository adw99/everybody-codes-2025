import sys
from typing import List,Tuple
from grid import Grid
from collections import deque
from functools import lru_cache,cache


def build_walls(walls: List[str]) -> Grid:

    movement = [(0,-1),(1,0),(0,1),(-1,0)]
    change_dir = { 'L': -1, 'R': 1}
    dir = 0 # aka 'up'
    x = 0
    y = 0
    path = [(x,y,'S')] # Lets begin at the beginning - Frank Turner
    for w in walls:
        cd = w[0]
        d = int(w[1])
        dir += change_dir[cd] # turn right or left
        dir = dir % len(movement)
        (dx,dy) = movement[dir]
        for _ in range(d):
            x += dx
            y += dy
            path.append( (x,y,'#'))
    # add the end point
    (x,y,_) = path.pop()
    path.append((x,y,'E'))
    
    # normalize pts to all >=0
    xmin = xmax = ymin = ymax = 0
    for p in path:
        (x,y,_) = p
        if x<xmin:
            xmin = x
        if x>xmax:
            xmax=x
        if y<ymin:
            ymin = y
        if y>ymax:
            ymax = y

    if xmin<0:
        xm = abs(xmin)
        xmax += xm
        path = [ (x+xm,y,s) for (x,y,s) in path]
    if ymin<0:
        ym = abs(ymin)
        ymax += ym
        path = [ (x,y+ym,s) for (x,y,s) in path]

    grid = Grid(max_x=xmax+1, max_y=ymax+1)
    for (x,y,s) in path:
        grid.set(x,y,s)

    return grid

def find_start_end(grid: Grid) ->Tuple[Tuple[int,int],Tuple[int,int]]:
    s = (0,0)
    e = (0,0)
    for x in range(grid.x()):
        for y in range(grid.y()):
            if grid.get(x,y) == 'S':
                s = (x,y)
            elif grid.get(x,y) == 'E':
                e = (x,y)
    return (s,e)


def print_grid(grid:Grid):
    for y in range(grid.y()):
        for x in range(grid.x()):
            s = grid.get(x,y)
            print( f"{s}", end="" )
        print(' ')
    print(' ')

def print_grid2(grid:Grid):
    for y in range(grid.y()):
        for x in range(grid.x()):
            (s,d) = grid.get(x,y)
            if s in "SE#":
                print( f"{s}{s}", end="" )
            else:
                if d > 99:
                    print('++',end="")
                else:
                    print( f"{d:02d}", end="")
        print(' ')
    print(' ')


def dijkstra(g:Grid,start:Tuple[int,int],end:Tuple[int,int])->int:
    result = 0

    # need a new grid that represents state and distance
    grid = Grid(max_x=g.x(), max_y=g.y())
    for x in range(g.x()):
        for y in range(g.y()):
            s = g.get(x,y)
            grid.set(x,y,(s,99999))
    # start is zero
    (x,y) = start
    (ex,ey) = end

    grid.set(x,y,('S',0))
    print(f">> {grid.get(ex,ey)}")

    neighbours = [(1,0),(-1,0),(0,1),(0,-1)]
    queue = deque()
    queue.append( start )
    xmax = grid.x()-1
    ymax = grid.y()-1
    while(len(queue)>0):
        (x,y) = queue.popleft()
        (s,dist) = grid.get(x,y)
        d2 = dist + 1

        for (dx,dy) in neighbours:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= xmax and 0 <= ny <= ymax:
                (ns,ndist) = grid.get(nx,ny)
                if ns != '#':
                    if d2<ndist:
                        ndist = d2
                        grid.set(nx,ny,(ns,ndist))
                        queue.append((nx,ny))


    (ex,ey) = end
    (_,result) = grid.get(ex,ey)

    print_grid2(grid)
    print(f">> {grid.get(ex,ey)}")

    return result

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 15, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    walls = df.read().splitlines()[0].split(',')
    print(f"{walls  }")

    grid = build_walls(walls)
    print_grid(grid)
    (start,end) = find_start_end(grid)
    print(f">> {start} to {end}")

    length = dijkstra(grid,start,end)


    print(f"Shortest distance: {length}")

