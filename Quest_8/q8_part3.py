import sys
from typing import List,Tuple
from collections import Counter
from functools import cache

def count_knots( new_line: Tuple[int,int], lines: List[Tuple[int,int]]) -> int:
    (nl,nh) = new_line
    knots = 0
    for l in lines:
        if l != new_line:
            (ll,lh) = l
            if (ll < nl < lh and nh>lh) or (nl<ll and ll< nh < lh):
                knots += 1
    return knots

def solution(nails: int, order:List[int]) -> Tuple[int,int]:

    lines = []
    knots = 0
    for o in range(len(order)):
        if o>0:
            new_line = sorted( (order[o-1], order[o]))
            lines.append( new_line )
    print(f"Lines: {len(lines)}")

    crosses = []
    for l1 in range(1,nails+1):
        for l2 in range (l1+1,nails+1):
            l = (l1,l2)
            c = count_knots(l,lines)
            if (l1,l2) in lines:
                c += 1
            # print(f"{l}: {c}")
            crosses.append( { 'c': c, 'l': l})
            
    crosses.sort( key=lambda x:x['c'], reverse=True)
    opt = crosses[0]
    # print(f"Crosses: {crosses}")
    print(f"Optimal strike: {opt['l']}, cuts {opt['c']} strings")

    return opt['l']



if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 8, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    nails = int(lines[0])
    order = [int(x) for x in lines[1].split(',')]

    opt = solution(nails,order)
    print(f"Optimal strike: {opt}")