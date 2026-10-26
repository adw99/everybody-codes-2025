import sys
from typing import List,Tuple
from collections import Counter
from functools import cache

def count_knots( new_line: Tuple[int,int], lines: List[Tuple[int,int]]) -> int:
    (nl,nh) = new_line
    knots = 0
    for l in lines:
        crosses = []
        (ll,lh) = l
        if (ll < nl < lh and nh>lh) or (nl<ll and ll< nh < lh):
            knots += 1
            # crosses.append(l)
        # if len(crosses)>0:
        #     print(f"{new_line}: {crosses}")
    return knots

def solution(nails: int, order:List[int]) -> int:

    lines = []
    knots = 0
    for o in range(len(order)):
        if o>0:
            new_line = sorted( (order[o-1], order[o]))
            new_knots = count_knots(new_line, lines)
            # print(f"{new_line} : {new_knots}")
            knots += new_knots
            lines.append( new_line )
    

    print(f"Lines: {len(lines)}")

    return knots


if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 8, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    nails = int(lines[0])
    order = [int(x) for x in lines[1].split(',')]

    centers = solution(nails,order)
    print(f"{centers} knots are needed")