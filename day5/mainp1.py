import sys
import numpy as np
from itertools import product
from collections import defaultdict

def xrange(x1, x2):
    if x1 <= x2:
        return np.arange(x1, x2 + 1)
    return np.arange(x1, x2 - 1, -1)

def yrange(y1, y2):
    if y1 <= y2:
        return np.arange(y1, y2+1)
    return np.arange(y1, y2-1, -1)

def main(fname):
    start = []
    end = []
    d = defaultdict(int)
    with open(fname) as f:
        for line in f:
            start.append(line.split("->")[0].strip())
            end.append(line.split("->")[1].strip())

    for i in range(len(start)):
        x1, y1 = map(int, start[i].split(","))
        x2, y2 = map(int, end[i].split(","))
        if x1 == x2 or y1 == y2:
            x = xrange(x1, x2)
            y = yrange(y1, y2)
            for p in list(product(x, y)):
                d[p] += 1
    
    more_than_two = 0
    for k, v in d.items():
        if v > 1:
            more_than_two += 1

    print(more_than_two)

if __name__ == "__main__":
    main(sys.argv[1])
