import re
import sys
from typing import List

       
def clean(crates,remove):
    for c in remove:
        crates.remove(c)

def part1(crates:List[int]) -> int:
    crates.sort()
    print(f"Crates: {len(crates)}")
    print(f"50's: {crates.count(50)}") # there were a lot of 50's in the test data 
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
        pack_list.append(pack)
        clean(crates,pack)
    # for p in pack_list:
    #     print("[ ", end='')
    #     for c in p:
    #         print(f" {c} ", end ='')
    #     print(' ]')        
    return len(pack_list)



if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 3, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    crates = [ int(x) for x in lines[0].split(',')]
    result = part1( crates )
    print(f"Result: {result}")
