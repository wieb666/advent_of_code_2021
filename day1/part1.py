import sys

def read_file(fname):
    with open(fname) as f:
        mylist = f.read().splitlines()
    return list(map(int, mylist))

def main(data_file):
    n = 0
    l = read_file(data_file)
    n = [n+1 for i in range(len(l)) if l[i] > l[i-1]]
    print(len(n))

if __name__ == "__main__":
    main(sys.argv[1])
    