import sys
import numpy as np

def main(fname):
    with open(fname) as f:
        pos = list(map(int, f.readlines()[0].split(",")))

    lowest_fuel = None
    for i in range(len(pos)):
        fuel = [sum(range(abs(x-i)+1)) for x in pos]
        if not lowest_fuel:
            lowest_fuel = sum(fuel)
        if sum(fuel) < lowest_fuel:
            lowest_fuel = sum(fuel)
    print(lowest_fuel)

if __name__ == "__main__":
    main(sys.argv[1])
