import sys
import functools
from typing import List


def new_seg(sp:int,segments:List[dict]) -> dict:
    ns = dict(l=None, spine=sp, r=None)
    segments.append(ns)
    return ns

def nas(x:int) -> str:
    if x==None:
        return '.'
    else:
        return str(x)

def decode_spine(nums:List[int]):
    print(f"Nums: {nums}")

    segments = []
    curr = None
    while len(nums)>0:
        val = nums.pop(0)
        if len(segments) == 0:
            curr = new_seg(val,segments)
        else:
            placed = False
            for s in segments:
                if val<s["spine"] and s["l"] == None:
                    placed = True
                    s["l"] = val
                    break
                elif val>s["spine"] and s["r"] == None:
                    s["r"] = val
                    placed = True
                    break
            if not placed:
                new_seg(val,segments)
    print(f"Spine segments: {len(segments)}")       
    result = ''
    for s in segments:
        lvl = ('' if s['l']==None else str(s['l'])) + str(s['spine']) + ('' if s['r']==None else str(s['r']))
        print(f" {nas(s["l"])}..{nas(s["spine"])}..{nas(s["r"])}: {lvl}")
        s['level'] = int(lvl)
        result += str(s["spine"])
    return (int(result),segments)

def sword_compare(a,b):
    va = -1
    vb = -1
    if a['quality'] != b['quality']:
        va = a['quality']
        vb = b['quality']
    else:
        for i in range(len(a['row_scores'])):
            if a['row_scores'][i] != b['row_scores'][i]:
                va = a['row_scores'][i]
                vb = b['row_scores'][i]
                print(f"{va} vs {vb}")
                break
    if va == vb:
        va = a['id']
        vb = b['id']

    if va < vb:
        return -1
    elif va>vb:
        return 1
    else:
        return 0
    
def solution(lines:List[str]) -> int:
    swords = []
    print(f"Lines: {len(lines)}")
    for l in lines:
        if len(l.strip()) == 0:
            break      
        parts = l.split(':')
        id = int(parts[0])
        nums = [ int(x) for x in parts[1].split(',')]
        print(f">> {id}")
        (q,s) = decode_spine(nums)
        row_scores = [seg['level'] for seg in s]
        swords.append({
            "id": id,
            "quality": q,
            "segments": s,
            "row_scores": row_scores
        })
    sorted_swords = sorted(swords, key=functools.cmp_to_key(sword_compare), reverse=True)
    for ss in sorted_swords:
        print(f"## {ss['id']}")
    checksum = 0
    for i in range(len(sorted_swords)):
        checksum += sorted_swords[i]['id'] * (i+1)
    return checksum


if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 5, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    result = solution( lines )
    print(f"Result: {result}")