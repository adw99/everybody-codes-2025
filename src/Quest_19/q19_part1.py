import sys
from typing import List,Tuple
from functools import lru_cache,cache
import math
from grid import Grid


def build_grid(trip_list: List[List]) -> Grid:

    max_y = 0
    max_x = 0
    for (x,y,height) in trip_list:
        if (y + height) > max_y:
            max_y = (y + height)
        if x > max_x:
            max_x = x
    max_y += 2
    max_x += 2
    grid = Grid(max_x=max_x, max_y=max_y)
    grid.set(0,0,'S')
    for (x,py,height) in trip_list:
        for y in range(0,grid.y()):
            if y<py or y>(py+height):
                grid.set(x,y,'#')
    return grid

def print_grid(grid:Grid):
    for y in range(grid.y()-1,-1,-1):
        for x in range(0,grid.x()):
            print(grid.get(x,y), end="")
        print("")

def flap(grid,pos,repeat):
    (x,y) = pos
    for _ in range(repeat):
            x+=1
            y+=1
            grid.set(x,y,'^')
    return (x,y)

def glide(grid,pos,repeat):
    (x,y) = pos
    for _ in range(repeat):
            x+=1
            y-=1
            grid.set(x,y,'v')
    return (x,y)

def alternate(grid,pos,repeat,align):
    flaps = 0
    pairs = math.floor(repeat/2)
    for p in range(pairs):
        pos = flap(grid,pos,1)
        pos = glide(grid,pos,1)
        flaps += 1
    if repeat % 2 == 1:
        if align == 1:
            pos = flap(grid,pos,1)
            flaps += 1
        else:
            pos = glide(grid,pos,1)
    return (pos,flaps)
    

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 19, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    if len(sys.argv) >=3:
        debug = True

    df = open(fname, "r")
    lines = df.read().splitlines()

    trip_list = [[int(x) for x in l.split(',')] for l in lines]

    grid = build_grid(trip_list)

    posx = posy = 0 # x,y or x,height
    flaps = 0
    for index,window in enumerate(trip_list):
        (wx,wy,wheight) = window
        dist = wx-posx

        if (index+1)<len(trip_list):
            (nx,ny,neight) = trip_list[index+1]
        else:
            nx = grid.x()
            ny = 0
            height = grid.y()

        align = 0
        if wy>posy:
            # we need to climb - climb to the bottom if next window is lower, else climb to top if possible
            target = (wy if (wy>ny) else ny) - posy
            dy = min(target,dist-1)
            (posx,posy) = flap(grid,(posx,posy),dy)
            flaps += dy
            dist -= dy
            align = 1
        elif posy>wy:
            target = posy-(wy+wheight) if ny>wy else posy-wy
            dy = min(target,dist-1)
            (posx,posy) = glide(grid,(posx,posy),dy)
            dist -= dy

        if dist>1:
            dc = dist-1
            # alternate flapping and gliding for the distance
            ((posx,posy),df) = alternate(grid,(posx,posy),dc,align)
            dist -= dc      
            flaps += df      
        if dist != 0:
            # options are flap or glide - default to glide if both are options
            gp = grid.get(posx+1,posy-1)
            if gp != '#':
                (posx,posy) = glide(grid,(posx,posy),1)
            else:
                (posx,posy) = flap(grid,(posx,posy),1)
                flaps += 1

        if not posy >= wy:
            print(f"?? MISSED ??")

    print_grid(grid)
    print(f"Total flaps: {flaps}")



