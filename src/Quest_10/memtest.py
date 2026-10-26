import sys
from grid import Grid
import time

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 10, Part 3 ***\n")

    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = [ l for l in df.read().splitlines() if len(l.strip())>0 ]
    max_x = len(lines[0])-1
    max_y = len(lines)-1
    print(f"Max: {max_x},{max_y}")
    grid = Grid(len(lines[0]), len(lines))
    print(f"Lines: {len(lines)}, grid: {grid.x()} x {grid.y()}")


    laps = 100000

    start_time = time.perf_counter()
    for _ in range(laps):
        _ = grid.deep_copy()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Deepcopy execution time: {elapsed_time:.6f} seconds")

    start_time = time.perf_counter()
    for _ in range(laps):
        _ = grid.manual_copy()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Manual copy execution time: {elapsed_time:.6f} seconds")    

    start_time = time.perf_counter()
    for _ in range(laps):
        _ = grid.pickle_copy()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Pickle copy execution time: {elapsed_time:.6f} seconds")        