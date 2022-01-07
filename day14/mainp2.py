from collections import Counter, defaultdict
import sys

def read_file(fname: str):
    template = None
    poly_d = defaultdict()
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if "->" in line:
                x, y = line.split(' -> ')
                poly_d[x] = y
            elif line:
                template = line.strip()
    return template, poly_d

def main(fname: str):
    
    template, poly_d = read_file(fname)
    print(template)
    
    pair_counts = Counter()
    for  i in range(0, len(template) - 1):
        pair_counts[template[i:i + 2]] += 1
    
    print(pair_counts)
    
    for _ in range(40):
        new_counts = Counter()
        char_counts = Counter()
        for k, v in pair_counts.items():
            new_counts[f"{k[0]}{poly_d[k]}"] += v
            new_counts[f"{poly_d[k]}{k[1]}"] += v
            
            char_counts[k[0]] += v
            char_counts[poly_d[k]] += v
        
        pair_counts = new_counts
    
    char_counts[template[-1]] += 1
        
    print(new_counts)
    print(char_counts)
    
    print(char_counts.most_common()[0][1] - char_counts.most_common()[-1][1])

if __name__ == "__main__":
    main(sys.argv[1])

#TODO The for loop is killing it.. stops after 18 loops

