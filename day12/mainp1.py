import sys
import collections

def main(fname):
    edges = collections.defaultdict(set)
    with open(fname) as f:
        for line in f:
            src, dst = line.strip().split("-")
            edges[src].add(dst)
            edges[dst].add(src)
    
    all_paths = set()
    todo = [('start',)]
    while todo:
        path = todo.pop()
        
        if path[-1] == 'end':
            all_paths.add(path)
        
        for cand in edges[path[-1]]:
            if not cand.islower() or cand not in path:
                # todo.append(path + (cand,))
                todo.append((*path, cand))

    print(len(all_paths))
    
if __name__ == "__main__":
    main(sys.argv[1])
