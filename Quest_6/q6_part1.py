import sys
from typing import List

def solution(input: str):
    fl = [ x for x in list(input) if x in 'aA']
    print(f"Fighters: {len(fl)}")
    mentors = 0
    total = 0
    for f in fl:
        if f == 'A':
            mentors += 1
        else:
            total += mentors
    return total

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 6, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    result = solution( lines[0] )
    print(f"Result: {result}")