import sys
from typing import List,Tuple
import re

# This is a *SPECIAL CASE* solution that handles the case where for each of the base (free branch) nodes
# all links to it are either positive or negative. It does not solve the general case, which is complicated
# by intervening nodes turning negative values into zeroes.

def calc_plant_energy(plant_list: List, mask: List[int], last_plant: int):

    unsolved = len(plant_list)
    pe_dict =  {}
    pe_dict = { x+1:mask[x] for x in range(len(mask))}
    while unsolved>0:
        for p in plant_list:
            plant_num = p["pn"]
            if plant_num not in pe_dict:
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
    return pe_dict[last_plant]

def solve_plant_tree(plant_list: List, last_plant: int)-> List[int]:
    base_layer = [p for p in plant_list if len(p["free_branches"]) >0 ]
    dep_plant_list = [p for p in plant_list if len(p["links"]) > 0 ]
    base_size = len(base_layer)

    solved = set( [ x["pn"] for x in base_layer] )

    # find the nodes that only depend on free branches
    second_layer = []
    higher_layers = []
    weights = {}
    for dp in dep_plant_list:
        links = dp["links"]
        deps = set( pn for (pn,_) in links)

        if deps.issubset(solved):
            mask = [0] * base_size
            for (pn,weight) in links:
                mask[pn-1] = weight
            weights[dp["pn"]] = mask
            second_layer.append(dp)
        else:
            higher_layers.append(dp)

    for n in second_layer:
        solved.add( n["pn"])
    print(f"Second layer: {second_layer}")


    # Find each layer 
    while len(higher_layers)>0:
        left = []
        found = []
        for dp in higher_layers:
            plant_num = dp["pn"]
            links = dp["links"]
            deps = set( pn for (pn,_) in links)
            if deps.issubset(solved):
                mask = [0] * base_size
                for (dpn,weight) in links:
                    dep_mask = weights[dpn]
                    for x in range(len(mask)):
                        mask[x] += weight * dep_mask[x]
                weights[plant_num] = mask
                found.append(plant_num)
            else:
                left.append(dp)
        higher_layers = left
        for n in found:
            solved.add(n)

    last_mask = weights[last_plant]

    pos_mask = [0] * len(last_mask)
    for x in range(len(last_mask)):
        pos_mask[x] = 1 if last_mask[x]>0 else 0
    print(f">> Last plant ({last_plant}): {pos_mask}")


    return pos_mask

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 18, Part 3 ***\n")
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

    print(f"^^ {plant_list}")
    last_plant = plant_list[-1]["pn"]
    dep_plant_list = [x for x in plant_list if len(x["free_branches"]) == 0]

    print(f"total plants: {len(plant_list)}")
    print(f"dependent plants: {len(dep_plant_list)}")

    max_mask = solve_plant_tree(plant_list, last_plant)
    max_energy = calc_plant_energy(dep_plant_list,max_mask,last_plant)
    print(f"Max energy: {max_energy} ({max_mask})")

    total = 0
    for tc in test_cases:
        result = calc_plant_energy(dep_plant_list,tc,last_plant)
        if result != 0:
            total += (max_energy-result)
        # print(f"{tc} -> {result}")
    print(f"Total energy difference: {total}")
