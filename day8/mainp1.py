import sys

def main(fname):
    n = 0
    with open(fname) as f:
        for line in f:
            line = [x.strip().split() for x in line.strip().split("|")]

            for i in line[1]:
                if len(i) in (2, 3, 4, 7):
                    n += 1
    
    print(n)

if __name__ == "__main__":
    main(sys.argv[1])
