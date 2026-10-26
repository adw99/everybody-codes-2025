import sys
from typing import List,Tuple


pos_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
max_x = 0
max_y = 0


def move_dragons(grid: List[List[dict]]) -> int:
    global pos_moves
    global max_x
    global max_y    

    count = 0
    # Find all dragons on grid, remove them from their old spots
    dragons = []
    for x in range(0,max_x+1):
        for y in range(0,max_y):
            pt = grid[x][y]
            if pt['dragon']:
                dragons.append((x,y))
                pt['dragon'] = False
    # print(f"Dragons: {len(dragons)}")

    # Now plot all possible moves from those spots
    for d in dragons:
        (x,y) = d
        for m in pos_moves:
            (dx,dy) = m
            newx = x + dx
            newy = y + dy
            if (0 <= newx <= max_x) and (0<= newy <= max_y):
                new_pt = grid[newx][newy]
                new_pt['dragon'] = True
                if new_pt['sheep'] and not new_pt['hideout']:
                    new_pt['sheep'] = False
                    count += 1
    return count

def move_sheep(grid:List[List[dict]]) -> int:
    count = 0
    escapes = 0
    for y in range(len(grid)-1,-1,-1):
        for x in range(0,len(grid[0])):
            pt = grid[x][y]
            if pt['sheep']:
                pt['sheep'] = False
                if y == max_y:
                    escapes += 1
                else:
                    new_pt = grid[x][y+1]
                    if new_pt['dragon'] and not new_pt['hideout']:
                        count += 1
                    else:
                        new_pt['sheep'] = True
    return count

def solution(moves: int, grid: List[List[int]] ) -> int:
    global max_x
    global max_y

    max_x = len(grid[0])-1
    max_y = len(grid)-1
    print(f"Max: {max_x},{max_y}")
    sheep = 0
    for x in range(moves):
        dx = move_dragons(grid)
        ds = move_sheep(grid)
        sheep += (dx+ds)
        print(f"Move: {x}, dx:{dx}, ds:{ds}")
    return sheep

def print_grid(grid:List[List[dict]]):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            pt = grid[x][y]
            if pt['dragon']:
                if pt['hideout'] and pt['sheep']:
                    print('*', end='')
                elif pt['hideout']:
                    print('d', end='')
                else:
                    print('D', end='')
            elif pt['sheep']:
                if pt['hideout']:
                    print('s', end='')
                else:
                    print('S', end='')
            elif pt['hideout']:
                print('#', end='')
            else:
                print('.', end='')
            

        print(' ')
    print(' ')


if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 10, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    moves = int(lines[0])    
    grid = [[' ' for _ in range(len(lines[1]))] for _ in range(len(lines)-1)]
    start = None
    for y in range(1,len(lines)):
        r = lines[y]
        if len(r.strip())>0:
            for x in range(len(r)):
                point = { 'dragon': False, 'sheep': False, 'hideout': False}
                grid[x][y-1] = point
                if r[x]=='D':
                    start = (x,y-1)
                    point['dragon']=True
                elif r[x] =='S':
                    point['sheep']=True
                elif r[x]=='#':
                    point['hideout']=True

    print_grid(grid)
    print(f"Dragon starts at: {start}")
    result = solution(moves,grid)
    print(f"Solution: {result}")
    # print_grid(grid)