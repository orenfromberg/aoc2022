rocks = set()
with open('./day14/data.txt') as f:
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

#calculate abyss, highest y value in rocks
abyss = 0
for rock in rocks:
    if(rock[1] > abyss):
        abyss = rock[1]

def new_sand():
    sandx, sandy = (500,0)

    while True:
        # look directly below
        if (sandx, sandy+1) not in rocks:
            sandy += 1
            if sandy > abyss:
                return False
            continue
        if(sandx-1, sandy+1) not in rocks:
            sandx -=1
            sandy +=1
            continue
        if(sandx+1, sandy+1) not in rocks:
            sandx += 1
            sandy += 1
            continue
        # it came to rest
        rocks.add((sandx,sandy))
        return True

count = 0
while new_sand():
    count += 1

print(count)