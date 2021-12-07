import sys
import numpy as np

def read_puzzle(file):
    with open(file) as f:
        return list(map(f.read().count, '012345678'))

def main(fname):
    puzzle = read_puzzle(fname)
    days = 256
    for _ in range(days):
        puzzle = puzzle[1:] + puzzle[:1]
        puzzle[6] += puzzle[-1]
    print(sum(puzzle))

if __name__ == "__main__":
    main(sys.argv[1])
