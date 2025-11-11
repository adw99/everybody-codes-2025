import re
import sys
from typing import List

def pack_crate(crates:List[int]) -> List[int]:
    pack = [crates[0]]
    last = pack[0]
    for c in crates:
        if c>last:
            pack.append(c)
            last = c
            if len(pack) == 20:
                return pack
    return pack
        


def part1(crates:List[int]) -> int:
    crates.sort()
    pack_list = []
    while len(crates)>0:
        pack = pack_crate(crates)
        for p in pack:
            crates.remove(p)
        if len(pack) == 20:
            print("[ ", end='')
            for c in pack:
                print(f" {c} ", end ='')
            print(' ]')
            return sum(pack)

    return -1

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 3, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    crates = [ int(x) for x in lines[0].split(',')]
    result = part1( crates )
    print(f"Result: {result}")
