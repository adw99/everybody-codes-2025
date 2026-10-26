import sys
from typing import List,Tuple

def validate_rule(name: str, rule:Tuple):
    index = 0
    (letter,conditions) = rule
    while index != -1:
        index = name.find(letter,index)
        if index != -1:
            nl = name[index+1]
            if not nl in conditions:
                print(f"{name} / {rule} -> Failed at {index}")
                return False
            index += 1
    print(f"{name} / {rule} -> Passed")
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
    
    return passing

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 7, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    names = lines[0].split(',')
    rules = lines[2:]
    result = solution( names,rules )
    print(f"Passing names: {result}")