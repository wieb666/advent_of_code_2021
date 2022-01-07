import sys
import heapq
from typing import Generator

def parse_coords_int(s: str):
    coords = {}
    for y, line in enumerate(s):
        for x, c in enumerate(line):
            coords[(x, y)] = int(c)
    return coords

def adjacent_4(x: int, y: int):
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y

def compute(s: str) -> int:
    coords = parse_coords_int(s)
    end = max(coords)
    seen = set()
    todo = [(0, (0, 0))]
    while todo:
        cost, last_coord = heapq.heappop(todo)

        if last_coord == end:
            return cost
        elif last_coord in seen:
            continue
        else:
            seen.add(last_coord)

        for cand in adjacent_4(*last_coord):
            if cand in coords:
                heapq.heappush(todo, (cost + coords[cand], cand))

    raise AssertionError('unreachable')

def main(fname: str):
    lines = []
    with open(fname) as f:
        for line in f:
            lines.append(line.strip())
    
    print(compute(lines))


if __name__ == "__main__":
    main(sys.argv[1])
