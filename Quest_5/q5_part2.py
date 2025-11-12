import sys
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

def decode_spine(nums:List[int]) -> str:
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
        print(f" {nas(s["l"])}..{nas(s["spine"])}..{nas(s["r"])}")
        result += str(s["spine"])
    return result

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
        swords.append({
            "id": id,
            "quality": int(decode_spine(nums))
        })
    sorted_swords = sorted(swords, key=lambda x: x['quality'])
    min = sorted_swords[0]
    max = sorted_swords[-1]
    print(f"Swords: {len(sorted_swords)}")
    print(f"Min quality: {min['id']} / {min['quality']}")
    print(f"Max quality: {max['id']} / {max['quality']}")
    result = max['quality'] - min['quality']
    return result


if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 5, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    result = solution( lines )
    print(f"Result: {result}")