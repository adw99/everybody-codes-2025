import sys
from typing import List,Tuple
from collections import Counter
from functools import cache

def count_common(str1 : str, str2: str) -> int:
    count = 0
    str_cmp = ''
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count +=1
            str_cmp += '+'
        else:
            str_cmp += ' '

    print(f"{str1}\r\n{str2}\r\n{str_cmp}\r\n{count}")
    return count

def cmp_dna(dna: dict, c: int, p1: int, p2:int) -> bool: 
    child = dna[c]
    par1 = dna[p1]
    par2 = dna[p2]
    for i in range(len(dna[1])):
        if child[i] != par1[i] and child[i] != par2[i]:
            return False
    return True

def find_child(dna: dict) -> int:
    c1 = cmp_dna(dna,1,2,3)
    c2 = cmp_dna(dna,2,1,3)
    c3 = cmp_dna(dna,3,1,2)
    print(f"Results: {c1} {c2} {c3}")
    return 1 if c1 else 2 if c2 else 3

def solution(dna: dict) -> int:
    dna_set = {1,2,3}
    child = find_child(dna)
    print(f"Child is {child}")
    dna_set.remove(child)
    vals = []
    for p in list(dna_set):
        vals.append(count_common(dna[child], dna[p]))
    print(f">> {vals}")

    return vals[0] * vals[1]


if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 9, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    dna = {}
    for l in lines:
        if len(l.strip())>0:
            parts = l.split(':')
            dna[int(parts[0])] = parts[1]

    result = solution(dna)
    print(f"Solution: {result}")
