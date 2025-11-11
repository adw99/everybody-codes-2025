from typing import Tuple
import sys


div = (100000,100000)
def c_mult(x: Tuple[int,int], y:Tuple[int,int] ) -> Tuple[int,int]:
    return ( (x[0]*y[0]) - (x[1]*y[1]),  (x[0]*y[1]) + (y[0]*x[1]) )

def c_add(x: Tuple[int,int], y:Tuple[int,int] ) -> Tuple[int,int]:
    return ( x[0]+y[0], x[1]+y[1])

def c_div(x: Tuple[int,int], y:Tuple[int,int] ) -> Tuple[int,int]:
    return ( neg_div(x[0],y[0]), neg_div(x[1],y[1]) )

def crunch(x: Tuple[int,int], a:Tuple[int,int]) -> Tuple[int,int]:
    x0 = x[0]
    x1 = x[1]
    d0 = div[0]
    return ( ((x0*x0) - (x1*x1)//d0)+a[0],
             ((x0*x1*2)//d0)+a[1] )


    # return ( (( (x[0]* x[0]) -  (x[1]*x[1])) /div[0] ) +y[0],
    #         ((x[0] * x[1] * 2)/div[1])+y[1])

def neg_div(a: int, b: int) -> int:
    if a > 0:
        return a // b
    return (a + b - 1) // b

def calculate_point(a: Tuple[int,int] ) -> bool:
    result = (0,0)
    # print(f"({a[0]},{a[1]})")
    d0 = div[0]
    for i in range(100):
        # prxint(f"...{i}:({result[0]},{result[1]})")
        # x0 = result[0]
        # x1 = result[1]
        # result = ( neg_div( ((x0*x0) - (x1*x1)),d0 ) + a[0],
        #         neg_div( (x0*x1*2), d0 ) + a[1] )

        result = c_mult(result,result)
        result = c_div(result,div)
        result = c_add(result, a)
        if abs(result[0])>1000000 or abs(result[1])>1000000:
            return False
    return True if abs(result[0])<=1000000 and abs(result[1])<=1000000 else False
                

    return result
width = 1001
def part2(avals: str) -> Tuple[int,int]:
    a = [int(x) for x in avals.split(',')]
    count = 0
    dots = [['.' for _ in range(width)] for _ in range(width)]
    print(f"A={a}")
    for xp in range(width):
        for yp in range(width):
            x = a[0] + xp
            y = a[1] + yp
            res = calculate_point( (x,y) )
            # print(f"({x},{y}) => {res}")
            if res:
                count += 1
                dots[xp][yp] = 'X'
    for row in range(width):
        for col in range(width):
            print(f"{dots[row][col]}", end='')
        print('')
    print(f"Points engraved: {count}")

if __name__ == '__main__':
    print(f"*** Everybody Codes 2025, Quest 2, Part 3 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample2.txt'
    df = open(fname, "r")
    lines = df.read().splitlines()
    part2( lines[0] )