import re
import sys


debug = False

def parse_move(move:str):
    rule_rex = re.compile("([RL])(\\d*)")
    res = rule_rex.search(move)
    return (res[1],  int(res[2]))

def part1( names_str: str, moves_str: str) -> str:
    names = names_str.split(',')
    moves = moves_str.split(',')
    max = len(names)-1
    state = 0

    for m in moves:
        (d,l) = parse_move(m)
        max_move = state if d=='L' else max-state
        mv = min(l,max_move) * (-1 if d=='L' else 1)
        state += mv
    
    print(f"Final state: {state} / {names[state]}")

    return names[state]

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Part 1 ***\n")
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    part1( lines[0], lines[1] )