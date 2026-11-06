import sys
from typing import List,Tuple
from collections import deque
from functools import lru_cache,cache
import math
from collections import defaultdict
from queue import PriorityQueue

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

    def is_wall(self,x,y):
        horz = vert = False

        horz = self.is_horz_wall(x,y)
        if not horz:
            vert = self.is_vert_wall(x,y)

        return horz or vert

def pos_key(pos: Tuple[int,int]) -> str:
    return str(pos[0]) + "_" + str(pos[1])

def manhattan_dist(a:Tuple[int,int], b:Tuple[int,int]) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def equal_points(a:Tuple[int,int], b:Tuple[int,int]) -> bool:
    return a[0] == b[0] and a[1] == b[1]

def solve_astar(sg:SparseGrid) ->int:
    (sx,sy) = sg.start
    (ex,ey) = sg.end
    print( f"{sx},{sy} -> {ex},{ey}")

    open_set = PriorityQueue()
    open_set.put( ((sx,sy),0) )

    came_from = {}

    g_score = defaultdict(lambda: float("inf"))
    g_score[pos_key(sg.start)] = 0

    f_score = defaultdict(lambda: float("inf"))
    f_score[pos_key(sg.start)] = manhattan_dist(sg.start,sg.end)

    while open_set.qsize()>0:
        (current,c_score) = open_set.get()
        if equal_points(current,sg.end):
            return c_score
        (x,y) = current
        for m in sg.movement:
            (dx,dy) = m
            nx = x + dx
            ny = y + dy
            n_score = c_score + 1
            p_key = pos_key( (nx,ny) )
            if not sg.is_wall(nx,ny):
                if n_score < g_score[p_key]:
                    came_from[p_key] = current
                    g_score[p_key] = n_score
                    f_score[p_key] = n_score + manhattan_dist( (nx,ny), sg.end )
                    if (nx,ny) not in open_set.queue:
                        open_set.put( ((nx,ny),n_score) )
            elif equal_points( (nx,ny), sg.end):
                return n_score

    # Not supposed to get here
    return math.inf

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


    length = math.inf
    length = solve_astar(sg)

    print(f"Shortest distance: {length}")

