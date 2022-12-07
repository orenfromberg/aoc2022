# dirs = {'/': {'a': {'e': {'i': 584}, 'f': 29116, 'g': 2557, 'h.lst': 62596}, 'b.txt': 14848514, 'c.dat': 8504156, 'd': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}}
fs = {}
stack = []
def process_command(line, stack):
    tokens = line.split()
    if(tokens[1] == 'cd'):
        if(tokens[2] == '/'):
            stack = []
        elif(tokens[2] == '..'):
            stack.pop()
        else:
            stack.append(tokens[2])

def compute_size(fs, stack):
    total = 0
    for i in fs:
        if(isinstance(fs[i], int)):
            total += fs[i]
        elif(isinstance(fs[i], dict)):
            total += compute_size(fs, stack)
    print(total)
    return total

with open('./day07/data.txt') as f:
    for line in f:
        tokens = line.split()
        if (tokens[0] == '$'):
            process_command(line, stack)
        elif (tokens[0] == 'dir'):
            foo = fs
            for i in stack:
                foo = foo[i]
            foo[tokens[1]] = {}
        else:
            foo = fs
            for i in stack:
                foo = foo[i]
            foo[tokens[1]] = int(tokens[0])

    # recurse through the dictionary and compute dir sizes
    compute_size(fs, stack)