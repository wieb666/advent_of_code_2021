import sys

def print_points(points):
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) in points:
                print("#", end="")
            else:
                print(" ", end="")
        print()

def main(fname: str):
    positions = set()
    instructions = []

    with open(fname) as f:
        for line in f:
            line = line.strip()
            if line.startswith("fold"):
                instructions.append(line)
            elif line:
                x, y = line.split(",")
                positions.add((int(x), int(y)))

    # print_points(positions)

    for line in instructions:
        instructions_s, n_s = line.split("=")
        axis = instructions_s[-1]
        n = int(n_s)
        
        if axis == "x":
            positions = { (x if x < n else n - (x - n), y,) for x, y in positions }
        elif axis == "y":
            positions = { (x, y if y < n else n - (y - n),) for x, y in positions }

    # print(len(positions))
    print_points(positions)

if __name__ == "__main__":
    main(sys.argv[1])
