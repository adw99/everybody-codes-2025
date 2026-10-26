import sys
from typing import List,Tuple
from collections import Counter
from functools import cache

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

def check_all_rules(name, rule_list):
    for r in rule_list:
        chk = validate_rule(name,r)
        if not chk:
            return False
    return True

def expand_name(name: str) -> List[str]:
    passing = []
    sfxs = []
    print(f"> {name}")
    last = name[-1]
    name = name [:-1]
    if last in triggers:
        sfxs += expand_suffix(last,name_max-len(name))        

    for s in sfxs:
        nn = name + s
        if name_min <= len(nn) <= name_max:
            passing.append(nn)
    print(f"== {len(passing)}")
    return passing


@cache
def expand_suffix(ltr : str, space: int) -> List[str]:
    passing = [ltr]
    if ltr in triggers and space>0:
        conditions = rules[ltr]
        for c in conditions:
            # print(f"{ltr} -> {c} ({space})")
            passing += [ltr + sfx for sfx in expand_suffix(c,space-1)]
    return passing



def check_list(l: List[str]):
    # Create a Counter object from the list
    element_counts = Counter(l)
    # Identify and count duplicates
    duplicates = {element: count for element, count in element_counts.items() if count > 1}
    print(f">>>> DUPES: {duplicates}")

name_min = 7
name_max = 11
rule_list = []
rules = {}
triggers = []

def solution(names: List[str], rules_raw: List[str]) -> List[str]:
    global rules , rule_list, triggers
    rules = dict()
    for r in rules_raw:
        parts = r.split('>')
        letter = parts[0].strip()
        conditions = parts[1].strip().split(',')
        rules[letter] = conditions
        rule_list.append( (letter,conditions))
        triggers.append(letter)

    print(f"Rule list: {rule_list}")
    print(f"Triggers: {triggers}")
    print(f"Rules: {rules}")


    passing = []
    for n in names:       
        if check_all_rules(n,rule_list):
            passing += expand_name(n)
        else:
            print(f"Name {n} failed precondition check")
    
    print(f"<Deduping....")
    passing = list(set(passing))
    print(f"...>")
    return passing

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 7, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    names = lines[0].split(',')
    rules = lines[2:]
    print(f"Names: {len(names)}, rules: {len(rules)}")
    passing = solution( names,rules )
    # passing = sorted(passing, key=lambda x:(len(x), x))
    # for p in passing:
    #     print(f"{p}")
    print(f"Passing names ({len(passing)})")
