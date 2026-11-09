import sys
from typing import List,Tuple
from collections import deque
from functools import lru_cache,cache
import math
from collections import defaultdict
from queue import PriorityQueue

import re


def calc_plant_energy(plant_list: List, plant_map: dict):

    unsolved = len(plant_list)

    while unsolved>0:
        for p in plant_list:
            if not "pe" in p:
                fb = p["free_branches"]
                if len(fb)>0:
                    p["pe"] = 1
                    unsolved -=1
                else:
                    pl = p["links"]
                    all_ready = True
                    incoming = 0
                    for (pn,th) in pl:
                        lp = plant_map[pn]
                        if "pe" in lp:
                            incoming += (th * lp["pe"])
                        else: 
                           all_ready = False
                    if all_ready:
                        th = p["thickness"]
                        p["pe"] = incoming if incoming>=th else 0
                        unsolved -=1
    return



if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 18, Part 1 ***\n")
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
    link_regex = re.compile("- branch to Plant (\\d*) with thickness (\\d*)")

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

    calc_plant_energy(plant_list,plant_map )
    last_plant = plant_list[-1]

    print(f"Final plant energy = {last_plant["pe"]}")
