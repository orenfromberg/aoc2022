def count_faces(droplets):
    faces = 0
    for drop in droplets:
        # check to see if adjacent drops are in the set
        x0,y0,z0 = drop
        count = 0
        for x,y,z in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            if (x0+x, y0+y, z0+z) in droplets:
                count += 1
        faces += 6 - count
    return faces

droplets = set()

filename = "./day18/data.txt"
# filename = "./day18/testdata.txt"
with open(filename) as f:
    for line in f:
        droplets.add(tuple([int(x) for x in line.strip().split(',')]))

# get bounding box of droplets
min_x = min([x for x,_,_ in droplets])-1
max_x = max([x for x,_,_ in droplets])+1
min_y = min([y for _,y,_ in droplets])-1
max_y = max([y for _,y,_ in droplets])+1
min_z = min([z for _,_,z in droplets])-1
max_z = max([z for _,_,z in droplets])+1

space = set()
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        for z in range(min_z, max_z+1):
            space.add((x,y,z))

# recursive will work for part 1 but not part 2 because 
# it will exceed stack depth.
def flood_fill(position):
    global space
    global droplets
    # global border
    x0,y0,z0 = position
    if position not in space or position in droplets:
        return
    if x0 < min_x or x0 > max_x or y0 < min_y or y0 > max_y or z0 < min_z or z0 > max_z:
        return
    space.remove(position)
    for x,y,z in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        print(f'flood_fill({x0+x},{y0+y},{z0+z}')
        flood_fill((x0+x,y0+y,z0+z))

def flood_fill2(position):
    global space
    global droplets
    q = []
    q.append(position)
    while(len(q)):
        position = q.pop(0)
        x0,y0,z0 = position
        if position not in space or position in droplets:
            continue
        if x0 < min_x or x0 > max_x or y0 < min_y or y0 > max_y or z0 < min_z or z0 > max_z:
            continue
        space.remove(position)
        for x,y,z in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            q.append((x0+x,y0+y,z0+z))

flood_fill2((min_x, min_y, min_z))
result = count_faces(space)
print(result)