import sys
from typing import List
import re


def calc_plant_energy(plant_list: List, plant_map: dict, test_case: List[int]):

    unsolved = len(plant_list)
    pe_dict =  {}
    while unsolved>0:
        for p in plant_list:
            plant_num = p["pn"]
            if plant_num not in pe_dict:
                fb = p["free_branches"]
                if len(fb)>0:
                    pe_dict[plant_num] = test_case[plant_num-1]
                    unsolved -= 1
                else:
                    pl = p["links"]
                    all_ready = True
                    incoming = 0
                    for (pn,th) in pl:
                        if pn in pe_dict:
                            incoming += (th * pe_dict[pn])
                        else: 
                           all_ready = False
                    if all_ready:
                        th = p["thickness"]
                        pe_dict[plant_num] = incoming if incoming>=th else 0
                        unsolved -=1
    return pe_dict



if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 18, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    if len(sys.argv) >=3:
        debug = True

    df = open(fname, "r")
    lines = df.read().splitlines()

    pn = 0
    plant_list = []
    plant_map = {}

    plant_regex = re.compile("Plant (\\d*) with thickness (\\d*)")
    free_branch_regex = re.compile("- free branch with thickness (\\d*)")
    link_regex = re.compile("- branch to Plant (\\d*) with thickness ([-+]?\\d*)")
    test_case_regex = re.compile("[(\\d) ]*")

    test_cases = []

    for l in lines:
        if l.startswith('Plant'):
            match = re.search(plant_regex,l)
            ld = match.groups()
            pn = int(ld[0])
            curr_plant = {
                "pn": pn,
                "thickness": int(ld[1]),
                "free_branches": [],
                "links": []
            }
            plant_list.append(curr_plant)
            plant_map[pn] = curr_plant
        elif l.startswith('-'):
            if 'free' in l:
                match = re.search(free_branch_regex,l)
                ld = match.groups()
                curr_plant["free_branches"].append(int(ld[0]))
            elif 'to Plant' in l:
                match = re.search(link_regex,l)
                ld = match.groups()
                link = ( int(ld[0]), int(ld[1]))
                curr_plant["links"].append(link)
        elif l.startswith('1') or l.startswith('0'):
            nums = l.replace(" ","")
            test_cases.append( [int(x) for x in nums])

    last_plant = plant_list[-1]["pn"]
    total = 0
    for tc in test_cases:
        pe_dict = calc_plant_energy(plant_list,plant_map,tc)
        result = pe_dict[last_plant]
        total += result
    print(f"Total energy: {total}")
