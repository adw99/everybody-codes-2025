import sys
from typing import List,Tuple
from collections import deque
from functools import lru_cache,cache
import math
from collections import defaultdict

debug = False

class SparseGrid():
   
    def __init__(self, start = None, end = None, horz_walls = None, vert_walls = None ):
        start = (0,0)
        end = (0,0)
        # using a grid system where (0,0) is meant to be the top left hand corner of the plane, y increases as we go 'down',
        # x increases as we go 'right'. (similar to grid.py) This keeps all coordinates as positive integers
        movement = [(0,-1),(1,0),(0,1),(-1,0)] # 0 = 'up', 1 = 'right', 2 = 'down' right, 3 = 'left';
        change_dir = { 'L': -1, 'R': 1}
        dir = 0 # aka 'up'

        vert_walls = []
        horz_walls = []

        x = y = 0
        last = 0
        for w in walls:
            cd = w[0]
            dist = int(w[1:])
            dir += change_dir[cd] # turn right or left
            dir = dir % len(movement)
            (dx,dy) = movement[dir]

            if dir % 2 == 0:
                # vertical wall
                if dy == 1:
                    ws = (x,y,y+(dist*dy))
                else:
                    ws = (x,y+(dist*dy),y)
                vert_walls.append( ws)
                # print(f"Vert wall: ({cd}-{dir}) {x}, {ws[1]}-{ws[2]}")
                y += (dy*dist)
                last = 0            
            else:
                #horizontal wall
                if dx == 1:
                    ws = (y,x,x+(dist*dx))
                else:
                    ws = (y,x+(dist*dx),x)
                horz_walls.append( ws )
                # print(f"Horz wall: ({cd}-{dir}) {ws[1]}-{ws[2]},{y}")
                x += (dx*dist)
                last = 1
        min_x = min_y = max_x = max_y = 0
        end = (x,y)

        for w in horz_walls:
            (_,x1,x2) = w
            if x1 < min_x:
                min_x = x1
            if x2 > max_x:
                max_x = x2

        for w in vert_walls:
            (_,y1,y2) = w
            if y1 < min_y:
                min_y = y1
            if y2 > max_y:
                max_y = y2

        # Align everything into positive coordinates, to make it easier on my brain
        dx = dy = 0
        if min_x < 0:
            dx = abs(min_x)
            horz_walls = [ (y,x1+dx,x2+dx) for (y,x1,x2) in horz_walls]
            vert_walls = [ (x+dx,y1,y2) for (x,y1,y2) in vert_walls]
            (x,y) = start
            start = ( x+dx,y)
            (x,y) = end
            end = (x+dx,y)
            max_x += dx
            

        if min_y < 0:
            dy = abs(min_y)
            horz_walls = [ (y+dy,x1,x2) for (y,x1,x2) in horz_walls]
            vert_walls = [ (x,y1+dy,y2+dy) for (x,y1,y2) in vert_walls]
            (x,y) = start
            start = (x,y+dy)
            (x,y) = end
            end = (x,y+dy)
            max_y += dy



        self.xmax = max_x
        self.ymax = max_y
        self.movement = movement


        print(f"Shifted grid by {dx},{dy}")
        print(f"Max: {self.xmax},{self.ymax}")

        self.start = start
        self.end = end
        self.horz_walls = horz_walls
        self.vert_walls = vert_walls

        self.horz_map = defaultdict(list)
        self.vert_map = defaultdict(list)


        if self.horz_walls != None:
            for (y,x_start,x_end) in self.horz_walls:
                self.horz_map[y].append( (x_start,x_end))

        if self.vert_walls != None:
            for (x,y_start,y_end) in self.vert_walls:
                self.vert_map[x].append( (y_start,y_end))


    def is_dir_vert(self,dir):
        return dir % 2 == 0 

    def is_vert_wall(self,x,y):
        # treat out of bounds as a wall
        if x == -1 or x == (self.xmax+1):
            return True
        for w in self.vert_map[x]:
            (y1,y2) = w
            if y1 <= y <= y2:
                return True
        return False

    def next_to_end(self,x,y):
        (ex,ey) = self.end
        man_dist = abs(ex-x) + abs(ey-y)
        return man_dist <=1


    def is_horz_wall(self,x,y):
        # treat out of bounds as a wall
        if y == -1 or y == (self.ymax+1):
            return True
        for w in self.horz_map[y]:
            (x1,x2) = w
            if x1 <= x <= x2:
                return True
        return False



def solve(sg:SparseGrid) ->int:
    result = split(sg,sg.start,-1,0)
    return result

def split(sg:SparseGrid, pos:Tuple[int,int], dir:int, dist:int) -> int:
    arb_limit = sg.xmax + sg.ymax
    if dist>arb_limit:
        return math.inf
    length = math.inf
    if debug:
        print(f">> split{pos}")
    pause()
    # Try every direction that is not a wall:
    (sx,sy) = pos
    opp_dir = (dir + 2) % len(sg.movement) if dir>0 else -1
    for i in range(len(sg.movement)):
        if i != opp_dir:
            (dx,dy) = sg.movement[i]
            if sg.is_horz_wall(sx+dx,sy+dy):
                d1 = wall_hug(sg,(sx,sy+1),i,0,dist+1)
                d2 = wall_hug(sg,(sx,sy-1),i,2,dist+1)
                length = min([length,d1,d2])
            elif sg.is_vert_wall(sx+dx,sy+dy):
                d1 = wall_hug(sg,(sx+1,sy),i,3,dist+1)
                d2 = wall_hug(sg,(sx-1,sy),i,1,dist+1)
                length = min([length,d1,d2])
            else:
                dl = move(sg, (sx,sy), i, dist)
                # print(f"solve {sx},{sy}({i}):{dl}")
                if dl < length:
                    length = dl
            
    return length+dist

def wall_hug( sg:SparseGrid, pos:Tuple[int,int], dir: int, wall_side: int, dist: int):
    moves = 0
    (x,y) = pos
    if not ( 0 <= x <= sg.xmax and 0<=y<=sg.ymax):
        return math.inf
    (dx,dy) = sg.movement[dir]
    if debug:
        print(f">> wall_hug({x},{y})")
    pause()

    stopped = False
    while not stopped:
        x += dx
        y += dy
        moves += 1

        # we stop when the wall we were hugging ends, or the space in front of us is blocked
        # if we were moving verticall check for horizontal walls in next square, and vice versa
        nx = x + dx
        ny = y + dy
        if nx<0 or nx>sg.xmax or ny<0 or ny>sg.ymax:
            stopped = True
        else:
            if dir % 2 == 0:
                stopped = sg.is_horz_wall(x+dx,y+dy)
            else:
                stopped = sg.is_horz_wall(x+dx,y+dy)

        if not stopped:
            # check if our hugged wall ended
            (dwx,dwy) = sg.movement[wall_side]
            if dir % 2 == 0:
                stopped = not sg.is_vert_wall(x+dwx,y+dwy)
            else:
                stopped = not sg.is_horz_wall(x+dwx,y+dwy)
    # are we next to the end?
    if sg.next_to_end(x,y):
        return dist + moves + 1
    else:
        return split(sg,(x,y),dir,dist+moves)

def pause():
    # input("...")
    print(f"",end="")

def move( sg:SparseGrid, pos:Tuple[int,int], dir: int, dist: int):
    (x,y) = pos
    (dx,dy) = sg.movement[dir]

    if debug:
        print(f"move> {x},{y}({dir})")
    pause()

    moves = 0
    wall = False
    found_end = False
    vert_move = dy != 0
    while not wall and not found_end:
        moves += 1
        if vert_move:
            y += dy
            wall = sg.is_horz_wall(x,y)
        else:
            x += dx
            wall = sg.is_vert_wall(x,y)
        found_end = sg.next_to_end(x,y)
        # print(f"{x},{y} ({found_end})")
        if x>sg.xmax or y>sg.ymax or x<0 or y<0:
            # we've missed a wall and gone outside the grid, end this branch
            return(math.inf)
    d2 = moves + dist
    if found_end:
        return(d2+1)
    md = split(sg,(x,y),dir,d2)
    return md

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 15, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    if len(sys.argv) >=3:
        debug = True

    df = open(fname, "r")
    walls = df.read().splitlines()[0].split(',')
    if debug:
        print(f"{len(walls)}> {walls}")


    sg = SparseGrid(walls)

    (sx,sy) = sg.start
    (ex,ey) = sg.end
    print( f"{sx},{sy} -> {ex},{ey}")


    length = solve(sg)

    print(f"Shortest distance: {length}")

