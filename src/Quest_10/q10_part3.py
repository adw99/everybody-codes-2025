import sys
from typing import List,Tuple
from grid import Grid
from functools import lru_cache
import pretty_errors
import traceback

pos_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
max_x = 0
max_y = 0

# def copy_grid(grid: List[List[dict]]) -> List[List[dict]]:
#     return copy.deepcopy(grid)
pgridx = ['A','B','C','D','E','F']
pgridy = ['1','2','3','4','5','6']
debug = True
def print_move(a:str, b:int, c:int):
    return f"{a}>{pgridx[b]}{pgridy[c]} "


def find_sheep(grid:Grid) -> List[dict]:
    sheep = []
    for y in range(grid.y()):
        for x in range(grid.x()):
            pt = grid.get(x,y)
            if pt.sheep:
                _sheep = { 'x':x, 'y':y }
                sheep.append(_sheep)
    # print(f"Sheep:{len(sheep)}")
    return sheep

def find_dragon(grid:Grid) -> Tuple[int,int]:
    for y in range(grid.y()):
        for x in range(grid.x()):
            pt = grid.get(x,y)
            if pt.dragon:
                return(x,y)
    return(-1,-1)


def is_escape_path(x:int, y:int, grid:Grid) -> bool:
    escape = True
    for dy in range(y,max_y+1):
        pt = grid.get(x,dy)
        escape = escape and pt.hideout
    return escape

@lru_cache(maxsize=100000)
def move_sheep(grid:Grid) -> int:
    count = 0
    sheep = find_sheep(grid)
    if len(sheep) == 0:
        print(f"We shouldn't be here!!!")
    sheep_moves = 0
    sheep_exit = False
    for _sheep in sheep:
        x = _sheep['x']
        y = _sheep['y']
        if y<max_y and not is_escape_path(x,y+1,grid):
            _next = grid.get(x,y+1)
            if not _next.dragon or _next.hideout:
                sheep_moves += 1
                _ng = grid.copy()
                _op = _ng.get(x,y)
                _op.sheep=False
                _np = _ng.get(x,y+1)
                _np.sheep=True
                # print_grid(_ng)
                count += move_dragon(_ng)
        else:
            # if " ESCAPED "  in path:
            #     print("\r\r\r")
            #     print_grid(grid)
            #     print(f"x2: {path} + ({print_move("S",x,y+1)})")
            #     print(" ************ ")
            #     print(" ???????????? ")
            #     sys.exit()
            #path = path + print_move("S",x,y+1) + " ESCAPED \r\r"
            #print(path)
            sheep_exit = True
    sheep_left = find_sheep(grid)
    # print(f"Sheep exit: {len(sheep_left)} / {sheep_moves}")
    if len(sheep_left)>0 and sheep_moves == 0 and not sheep_exit:
        # path = path + ">Sheep no op "
        if debug:
            print(f">Sheep no op ")
            print_grid(grid)
        count += move_dragon(grid)
    return count

@lru_cache(maxsize=100000)
def move_dragon(grid: Grid) -> int:
    global pos_moves
    global max_x
    global max_y    

    count = 0
    (x,y) = find_dragon(grid)

    # Now plot all possible moves from those spots
    for m in pos_moves:
        (dx,dy) = m
        newx = x + dx
        newy = y + dy
        if (0 <= newx <= max_x) and (0<= newy <= max_y):
            _ng = grid.copy()
            _op = _ng.get(x,y)
            _op.dragon = False
            new_pt = _ng.get(newx,newy)
            new_pt.dragon = True
            if new_pt.sheep and not new_pt.hideout:
                new_pt.sheep = False
            # path = path + print_move("D",newx,newy)
            # print_grid(_ng)
            sheep = find_sheep(_ng)
            if len(sheep)==0:
                if debug:
                    print(f"*** Ate the last sheep! \r\r")
                # sys.exit()
                count += 1
            else:
                count += move_sheep(_ng)
    return count

def solution(grid: Grid ) -> int:
    result = move_sheep(grid)
    return result

def print_grid(grid:Grid):
    for y in range(grid.y()):
        for x in range(grid.x()):
            pt = grid.get(x,y)
            if pt.dragon:
                if pt.hideout and pt.sheep:
                    print('*', end='')
                elif pt.hideout:
                    print('d', end='')
                else:
                    print('D', end='')
            elif pt.sheep:
                if pt.hideout:
                    print('s', end='')
                else:
                    print('S', end='')
            elif pt.hideout:
                print('#', end='')
            else:
                print('.', end='')
        

        print(' ')
    print(' ')

class Point:
    def __init__(self,dragon=False,sheep=False,hideout=False):
        self.dragon = dragon
        self.sheep = sheep
        self.hideout = hideout
    def __eq__(self, value):
        return self.dragon == value.dragon and self.sheep == value.sheep and self.hideout == value.hideout
    def __hash__(self):
        return hash((self.dragon, self.sheep, self.hideout))

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 10, Part 3 ***\n")

    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample3.txt'
    df = open(fname, "r")
    lines = [ l for l in df.read().splitlines() if len(l.strip())>0 ]
    max_x = len(lines[0])-1
    max_y = len(lines)-1
    print(f"Max: {max_x},{max_y}")
    grid = Grid(max_x=len(lines[0]), max_y=len(lines))
    print(f"Lines: {len(lines)}, grid: {grid.x()} x {grid.y()}")
    start = None

    for y in range(len(lines)):
        r = lines[y]
        for x in range(len(r)):
            point = Point( r[x]=='D', r[x]=='S', r[x]=='#' )
            grid.set(x,y,point)
            if r[x] == 'D':
                start = (x,y-1)

    print_grid(grid)
    print(f"Dragon starts at: {start}")

    try:
        result = solution(grid)
        print(f"\r \rSolution: {result}")
    except Exception as e:
        print(f"Error: {e}")
        # print("Printing a shortened traceback (last 2 frames):")
        # traceback.print_exception(type(e), e, e.__traceback__, limit=2)
        print("\nPrinting the full traceback:")
        traceback.print_exc() # Prints the full traceback by default    
    


