import sys
import heapq
from typing import Generator

def parse_coords_int(s: str):
    coords = {}
    for y, line in enumerate(s):
        for x, c in enumerate(line):
            coords[(x, y)] = int(c)
    return coords

def weird_mod(n: int) -> int:
    while n > 9:
        n -= 9
    return n

def adjacent_4(x: int, y: int):
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y

def compute(s: str) -> int:
    coords = parse_coords_int(s)
    width, height = max(coords)
    width, height = width + 1, height + 1

    coords = {
        (x_i * width + x, y_i * height + y): weird_mod(n + x_i + y_i)
        for (x, y), n in tuple(coords.items())
        for y_i in range(5)
        for x_i in range(5)
    }

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
