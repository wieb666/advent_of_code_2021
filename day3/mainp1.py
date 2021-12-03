import sys

def main(fname):
    gamma = ""
    epsilon = ""
    with open(fname) as f:
        data = f.read().splitlines()
    data = [list(x) for x in data]
    # print(data)

    for i in range(len(data[0])):
        if [item[i] for item in data].count('0') > [item[i] for item in data].count('1'):
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"

    print(gamma)
    print(epsilon)
    print(int(gamma, 2) * int(epsilon, 2))            

if __name__ == "__main__":
    main(sys.argv[1])
