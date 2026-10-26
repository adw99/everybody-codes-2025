import sys
from typing import List,Tuple

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 11, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    cols = [int(l) for l in lines]

    mean = sum(cols) / len(cols) 
    print(f"Total: {sum(cols)}")
    print(f"Mean: {mean}")
    print(f"Cols: {len(cols)}")

    moves = 0
    for c in cols:
        diff = abs (mean - c)
        moves += diff/2 # moving one duck 'corrects' two columns by 1 each
    print(f"Moves: {moves}")