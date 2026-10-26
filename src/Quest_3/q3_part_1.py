import re
import sys
from typing import List

def countPack(pack:List[List[int]])->int:
    max = 0
    for pl in pack:
        count = 0
        for c in pl:
            count += c
        if count>max:
            max = count
    return max

def part1(crates:List[int]) -> int:
    crates.sort()
    pack_list = []
    while len(crates)>0:
        pack = []
        first = crates[0]
        pack.append(first)
        last = first
        for c in crates:
            if c>last:
                pack.append(c)
                last = c
        for p in pack:
            crates.remove(p)
        pack_list.append(pack)

    for p in pack_list:
        print("[ ", end='')
        for c in p:
            print(f" {c} ", end ='')
        print(' ]')
    return countPack(pack_list)

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 3, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    crates = [ int(x) for x in lines[0].split(',')]
    result = part1( crates )
    print(f"Result: {result}")
