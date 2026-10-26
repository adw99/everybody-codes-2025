import sys
from typing import List,Tuple
from collections import Counter
from functools import cache

def solution(nails: int, order:List[int]) -> int:

    pegs = [x+1 for x in range(nails)]
    half = nails/2
    opposites = {}
    for p in pegs:
        op = int( (p+half)%nails )
        opposites[p] = nails if op == 0 else op
    print(f"Opposites: {opposites}")

    centres = 0
    for o in range(len(order)):
        if o>0:
            if opposites[order[o-1]] == order[o]:
                print(f"{order[o-1]} -> {order[o]}")
                centres += 1
            else:
                print(f"X {order[o-1]} -> {order[o]}")

    return centres


if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 8, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    nails = int(lines[0])
    order = [int(x) for x in lines[1].split(',')]

    centers = solution(nails,order)
    print(f"{centers} threads pass through the center")