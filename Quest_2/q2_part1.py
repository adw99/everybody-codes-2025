from typing import Tuple
import sys


def c_mult(x: Tuple[int,int], y:Tuple[int,int] ) -> Tuple[int,int]:
    return ( (x[0]*y[0]) - (x[1]*y[1]),  (x[0]*y[1]) + (y[0]*x[1]) )

def c_add(x: Tuple[int,int], y:Tuple[int,int] ) -> Tuple[int,int]:
    return ( x[0]+y[0], x[1]+y[1])

def c_div(x: Tuple[int,int], y:Tuple[int,int] ) -> Tuple[int,int]:
    return ( x[0]//y[0], x[1]//y[1])

def part1(avals: str) -> Tuple[int,int]:
    a = [int(x) for x in avals.split(',')]
    print(f"A={a}")
    result = (0,0)

    for i in range(3):
        result = c_mult(result,result)
        result = c_div(result,(10,10))
        result = c_add(result, a)
        print(f"{i}) result = [{result[0]},{result[1]}]")

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 2, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    part1( lines[0] )