import sys

def oxygen(data):
    while True:
        for i in range(len(data[0])):
            new_data = [item[i] for item in data]
            if new_data.count('0') > new_data.count('1'):
                new_data_index = [i for i, v in enumerate(new_data) if v == "0"]
            else:
                new_data_index = [i for i, v in enumerate(new_data) if v == "1"]
            data = [data[x] for x in new_data_index]
                
            if len(data) == 1:
                return "".join(data[0])

def co2(data):
    while True:
        for i in range(len(data[0])):
            new_data = [item[i] for item in data]
            if new_data.count('0') > new_data.count('1'):
                new_data_index = [i for i, v in enumerate(new_data) if v == "1"]
            else:
                new_data_index = [i for i, v in enumerate(new_data) if v == "0"]
            data = [data[x] for x in new_data_index]
                
            if len(data) == 1:
                return "".join(data[0])
    

def main(fname):
    with open(fname) as f:
        data = f.read().splitlines()
    data = [list(x) for x in data]
    oxy = oxygen(data)
    co = co2(data)
    print(oxy)
    print(co)
    print(int(oxy, 2) * int(co, 2))

if __name__ == "__main__":
    main(sys.argv[1])
