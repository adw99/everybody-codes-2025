import sys
from typing import List,Tuple

debug = False

def print_cols(cols: List):
    pc = ""
    for c in cols:
        pc += f"{c} "
    return pc

def checksum(cols:List):
    checksum = 0
    for x in range(len(cols)):
        checksum += cols[x] * (x+1)
    return checksum

def balance(cols: List):
    complete = False
    round = 0
    while not complete:
        moves = 0
        for x in range(len(cols) -1 ):
            if cols[x] > cols[x+1]:
                cols[x] -=1
                cols[x+1] +=1
                moves += 1 
        if debug:
            print(f"Round {round}, {moves} moves: {print_cols(cols)} {checksum(cols)}")
        if moves == 0:
             complete=True
        else:
            round += 1

    complete = False
    while not complete:
        moves = 0
        for x in range(len(cols) -1 ):
             if cols[x+1] > cols[x]:
                  cols[x+1] -=1
                  cols[x] +=1 
                  moves += 1
        if debug:
            print(f"Round {round}, {moves} moves: {print_cols(cols)} {checksum(cols)}")

        if moves == 0:
            complete = True
        else:
            round += 1

    print(f"Round {round}, {moves} moves: {print_cols(cols)} {checksum(cols)}")

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 11, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    cols = [int(l) for l in lines]

    print(print_cols(cols))

    balance(cols)
