import sys
import numpy as np

def main(fname):
    with open(fname) as f:
        for line in f:
            fish = np.array(list(map(int, line.strip().split(","))))
    print(fish)
    
    days = 80
    day = 0
    
    while day < days:
        if 0 not in fish:
            fish = fish - 1
        else:
            n_new_fish = np.count_nonzero(fish == 0)
            fish[fish == 0] = 7
            fish = np.append(fish, [9] * n_new_fish)
            fish = fish - 1
        day += 1

    print(len(fish))


if __name__ == "__main__":
    main(sys.argv[1])
