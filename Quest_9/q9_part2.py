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

    # print(f"{str1}\r\n{str2}\r\n{str_cmp}\r\n{count}")
    return count

def calc_similarity(dna: dict, child:int, p1: int, p2: int) -> int:
    v1 = count_common(dna[child], dna[p1])
    v2 = count_common(dna[child], dna[p2])
    return v1*v2

def cmp_dna(dna: dict, c: int, p1: int, p2:int) -> bool: 
    child = dna[c]
    par1 = dna[p1]
    par2 = dna[p2]
    for i in range(len(dna[1])):
        if child[i] != par1[i] and child[i] != par2[i]:
            return False
    return True

def find_child(dna: dict,x:int,y:int,z:int) -> int:
    c1 = cmp_dna(dna,x,y,z)
    c2 = cmp_dna(dna,y,x,z)
    c3 = cmp_dna(dna,z,x,y)
    # print(f"Results: {c1} {c2} {c3}")
    return (x, [y,z]) if c1 else (y, [x,z]) if c2 else (z, [x,y]) if c3 else (-1,[])


def find_parents(dna:dict, found:List[int]) -> Tuple:
    ducks = len(dna)
    for x in range(1,ducks+1):
        for y in range(2,ducks+1):
            for z in range(3,ducks+1):
                if (x!=y and x!=z and y!=z) and not (x in found or y in found or z in found):
                    (child,parents) = find_child(dna,x,y,z)
                    if child != -1:
                        return (child,parents)
    return (-1,[])

def solution(dna: dict) -> int:
    found = []
    found_app_parents = False
    families = []
    while not found_app_parents:
        (child,parents) = find_parents(dna, found)
        if child == -1:
            found_app_parents = True
        else:
            print(f">> {child} -> {parents}")
            found.append(child)
            found.append(parents[0])
            found.append(parents[1])
            families.append( (parents, [child]))

    print(f"Families: {families}")

    # find remaining children and associate them with families
    all_dna = set(dna.keys())
    found_dna = set(found)
    kids = all_dna.difference(found_dna)
    print(f"Missing kids: {kids}")

    for k in list(kids):
        for f in families:
            (parents,_) = f
            (child,parents) = find_child(dna,k,parents[0],parents[1])
            if child == k:
                print(f"{k} -> {parents}")
                f[1].append(k)
                break

    print(f"Families: {families}")

    total = 0
    for f in families:
        (parents,children) = f
        for c in children:
            total += calc_similarity(dna,c,parents[0],parents[1])
    return total

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 9, Part 2 ***\n")
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
