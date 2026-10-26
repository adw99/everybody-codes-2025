import sys
from typing import List

def solution(input: str):
    pairs = [ 'Aa', 'Bb', 'Cc']
    result = 0
    for p in pairs:
        mentors = 0
        total = 0
        fl = [ x for x in list(input) if x in p]
        print(f"Fighters: {len(fl)}")
        for f in fl:
            if f.isupper():
                mentors += 1
            else:
                total += mentors
        result += total
    return result

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 6, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    result = solution( lines[0] )
    print(f"Result: {result}")