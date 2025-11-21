import sys
from typing import List,Tuple
from collections import Counter
from functools import cache

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

def new_node(id:int) -> dict:
    return {
        'id': id,
        'parents': [],
        'children': []
    }

def update_nodes( graph:dict, child:int, parents:List[int]):
    exists = graph.keys()
    if child not in exists:
        graph[child] = new_node(child)
    graph[child]['parents'] = parents

    for p in parents:
        if p not in exists:
            graph[p] = new_node(p)
        if child not in graph[p]['children']:
            graph[p]['children'].append(child)

def find_parents(dna:dict) -> dict:
    ducks = len(dna)
    results = {}
    count = 0
    for x in range(1,ducks+1):
        for y in range(1,ducks+1):
            for z in range(1,ducks+1):
                if (x!=y and x!=z and y!=z):
                    (child,parents) = find_child(dna,x,y,z)                    
                    if child != -1:
                        count += 1
                        update_nodes(results,child,parents)
                        print(f"{x},{y},{z}")

    print(f">> {count} child/parents found")
    return results

def add_fam_member(fam:set, dd:Tuple) -> List[int]:
    fam.add(dd['id'])
    links = []
    for p in dd['parents']:
        fam.add(p)
        links.append(p)
    for c in dd['children']:
        fam.add(c)
        links.append(c)
    return links

def find_family(ids: List[int], nodes: dict) -> List[int]:
    fam = set()
    start = -1
    opts = list(nodes)
    opts.sort()
    print(f"****> {opts}")
    for idx in range(len(ids)):
        start = ids[idx]
        if start in opts:
            break
    print(f"Start> {start}")
    if not start in opts:
        return []
    
    links = add_fam_member(fam, nodes[start])
    ids.remove(start)
    while len(links)>0:
        id = links.pop(0)
        if id in ids:
            next = nodes[id]
            ids.remove(id)
            links += add_fam_member(fam, next)
    return list(fam)


def solution(dna: dict) -> int:
    found = []
    found_app_parents = False
    families = []
    print(f"Building graph map.....")
    graph_map = find_parents(dna)

    print(f"Check: {len(dna)} vs {len(graph_map)}")

    print(f"Finding families")
    ids = list(dna.keys())
    while len(ids)>0:
        f = find_family(ids, graph_map)
        if len(f)>0:
            families.append(f)
            print(f"Family -> {f}")
        else:
            break

    families = sorted(families, key = lambda x:len(x))
    lf = families[-1]
    print(f"Largest family: {len(lf)} / {lf}")
    return sum(lf)

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 9, Part 3 ***\n")
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
