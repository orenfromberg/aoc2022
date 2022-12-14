rocks = set()
with open('./day14/testdata.txt') as f:
    for _line in f:
        paths = [(int(y[0]),int(y[1])) for y in [x.split(',') for x in _line.strip().split(' -> ')]]
        for i in range(len(paths)-1):
            x0, y0 = paths[i]
            x1, y1 = paths[i+1]
            stepx = 1 if x1 > x0 else -1
            stepy = 1 if y1 > y0 else -1
            for x in range(x0,x1+stepx,stepx):
                for y in range(y0,y1+stepy,stepy):
                    rocks.add((x,y))

print(len(rocks))