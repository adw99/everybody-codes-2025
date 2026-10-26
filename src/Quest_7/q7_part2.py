import sys
from typing import List,Tuple

def validate_rule(name: str, rule:Tuple):
    index = 0
    max = len(name)-1
    (letter,conditions) = rule
    while index != -1 and index != max:
        index = name.find(letter,index)
        if index != -1 and index!=max:
            nl = name[index+1]
            if not nl in conditions:
                return False
            index += 1
    return True
            

def solution(names: List[str], rules_raw: List[str]) -> List[str]:
    rules = []    
    for r in rules_raw:
        parts = r.split('>')
        letter = parts[0].strip()
        conditions = parts[1].strip().split(',')
        rules.append( (letter,conditions))

    passing = []
    for n in names:
        passed = True
        for r in rules:
            passed = passed and validate_rule(n,r)
            if not passed:
                break
        if passed:
            passing.append(n)
    
    result = 0
    for n in passing:
        result += ( names.index(n) + 1)

    return (result,passing)

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 7, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    names = lines[0].split(',')
    rules = lines[2:]
    print(f"Names: {len(names)}, rules: {len(rules)}")
    (result,passing) = solution( names,rules )
    print(f"Passing names ({len(passing)}): {passing}")
    print(f"Checksum : {result}")