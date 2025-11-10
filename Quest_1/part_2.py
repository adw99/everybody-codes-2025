import re
import sys


def parse_move(move:str):
    rule_rex = re.compile("([RL])(\\d*)")
    res = rule_rex.search(move)
    return (res[1],  int(res[2]))

def part1( names_str: str, moves_str: str) -> str:
    names = names_str.split(',')
    moves = moves_str.split(',')
    max = len(names)
    state = 0
    print(f"{max} Names")
    for m in moves:
        (d,l) = parse_move(m)
        max_move = state if d=='L' else max-state
        new_state = -1
        print(f"# {state}, {d}{l}, {max_move}")
        if l>=max_move:
            print("WRAP")
            if d=='L':
                new_state = max - ( l-state % max )
            else:
                new_state = l-(max-state) % max
        else:
            mv = l * (-1 if d=='L' else 1)
            new_state = state + mv
        print(f"From {state}, {d}{l} -> {new_state} ({names[new_state]})")
        state = new_state
    
    print(f"Final state: {state} / {names[state]}")

    return names[state]

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample2.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    part1( lines[0], lines[1] )