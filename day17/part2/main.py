shapes = []
shapes.append([(0,0),(1,0),(2,0),(3,0)])
shapes.append([(1,0),(0,1),(1,1),(2,1),(1,2)])
shapes.append([(0,0),(1,0),(2,0),(2,1),(2,2)])
shapes.append([(0,0),(0,1),(0,2),(0,3)])
shapes.append([(0,0),(0,1),(1,0),(1,1)])
cur_shape = 0
jets = []
cur_jet = 0
tunnel = set()
tunnel_width = 7

# attempts to move and returns if successful or not
def translate(rock: list, vec: tuple, tunnel: set) -> bool:
    x0,y0 = vec
    new_rock = rock.copy()
    global tunnel_width
    for i, (x, y) in enumerate(new_rock):
        new_pos = ((x + x0, y + y0))
        if new_pos in tunnel:
            return False
        if new_pos[0] == 0 or new_pos[1] == 0:
            return False
        if new_pos[0] > tunnel_width:
            return False
        new_rock[i] = new_pos
    
    for i in range(len(rock)):
        rock[i] = new_rock[i]
    return True

# this will simulate a rock being dropped in the tunnel 
def drop_rock():
    global tunnel
    # get highest rock currently in set
    height = 0
    for rock in tunnel:
        height = rock[1] if rock[1] > height else height
    
    # place rock in space
    global shapes
    global cur_shape
    rock = shapes[cur_shape].copy()
    cur_shape = (cur_shape + 1) % len(shapes)

    # move to start
    translate(rock, (3,4+height), tunnel)
    # print(rock)

    global cur_jet
    global jets
    while(True):
        # move left or right
        direction = jets[cur_jet]
        cur_jet = (cur_jet + 1) % len(jets)
        if direction == '<':
            translate(rock, (-1,0), tunnel)
        else:
            translate(rock, (1,0), tunnel)
        
        # move down
        if not translate(rock, (0,-1), tunnel):
            # add rock to set
            for pixel in rock:
                tunnel.add(pixel)
            break

filename = './day17/data.txt'
# filename = './day17/testdata.txt'
with open(filename) as f:
    for line in f:
        jets = [x for x in line.strip()]


def get_max_height():
    global tunnel
    height = 0
    for rock in tunnel:
        height = rock[1] if rock[1] > height else height
    return height


# with open("out.txt","x") as f:
prev_height = 0
curr_height = 0
# print(jets)
for i in range(1000000000000):
    drop_rock()
    
    # print on the screen
    screen = [[' ' for col in range(8)] for row in range(11)]
    curr_height = get_max_height()
    subset = [(x,y) for x,y in tunnel if y > (curr_height - 10)]
    for x,y in subset:
        screen[y%10][x] = '#'
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            print(screen[10-y][x],end='')
        print('')
    print('\n')
    # for row in screen:
    #     for col in row:
    #         print(col,end='')
    #     print('')
    # print('\n')

    # if i % 1000 == 0:
    #     # clean the tunnel
    #     print(f'cleaning at {i}')
    #     new_tunnel = set()
    #     for x,y in tunnel:
    #         if y > .99*curr_height:
    #             # tunnel.remove((x,y))
    #             new_tunnel.add((x,y))
    #     tunnel = new_tunnel
    # f.write(f'{curr_height - prev_height} ')
    prev_height = curr_height
print(prev_height)