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

print(count_faces(droplets))