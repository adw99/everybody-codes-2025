import sys
from typing import List,Tuple


pos_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
max_x = 0
max_y = 0


def move_and_eat(pos:Tuple[int,int], moves:int, grid: List[List[int]]) -> int:
    global pos_moves
    global max_x
    global max_y    

    count = 0
    (x,y) = pos
    if grid[x][y] == 'S':
        count +=1
        grid[x][y] = 'X'
    if moves>0:
        for m in pos_moves:
            (dx,dy) = m
            newx = x + dx
            newy = y + dy
            if (0 <= newx <= max_x) and (0<= newy <= max_y):
                count += move_and_eat( (newx,newy), moves-1, grid)
    return count

def solution(start:Tuple[int,int], moves: int, grid: List[List[int]] ) -> int:
    global max_x
    global max_y

    max_x = len(grid[0])-1
    max_y = len(grid)-1
    print(f"Max: {max_x},{max_y}")

    sheep = move_and_eat(start,moves,grid)
    return sheep

def print_grid(grid:List[List[str]]):
    for y in range(len(grid)):
        for x in range(len(grid[0])):            
            print(f"{grid[x][y]}", end='')
        print(' ')
    print(' ')


if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 10, Part 1 ***\n")
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
                grid[x][y-1] = r[x]
                if r[x]=='D':
                    start = (x,y-1)

    print_grid(grid)
    print(f"Dragon starts at: {start}")
    result = solution(start,moves,grid)
    print(f"Solution: {result}")
    print_grid(grid)