import sys

def main(fname):
    horizontal, depth = 0, 0
    with open(fname) as f:
        for line in f:
            line = line.strip().split()
            value = int(line[1])
            if line[0] == "forward":
                horizontal += value
            elif line[0] == "up":
                depth += value
            elif line[0] == "down":
                depth -= value
    print(horizontal * abs(depth))

if __name__ == "__main__":
    main(sys.argv[1])
