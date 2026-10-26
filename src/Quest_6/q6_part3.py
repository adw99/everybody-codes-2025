import sys
from typing import List

window = 1000
repeats = 1000

def solution(input: str):
    people = list(input * repeats)
    print(f">People: {len(people)}")
    mentors_dict = {
        'a': 'A',
        'b': 'B',
        'c': 'C'        
    }
    result = 0
    percent = int(len(people)/100)
    for i in range(len(people)):
        if people[i].islower():
            start = max(i-window,0)
            end = min(i+window+1,len(people))
            neighbors = people[start:end]
            mentors = neighbors.count( mentors_dict[people[i]])
            # print(f"{i}) {people[i]}: {start} / {end} = {mentors}")
            if i % percent == 0:
                print(f">{i}")
            result += mentors
    return result

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 6, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    result = solution( lines[0] )
    print(f"Result: {result}")